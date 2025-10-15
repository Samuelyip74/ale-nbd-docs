Rail Transportation Network Design (Wired & Wireless, Trackside & Station)
=========================================================================

.. contents::
   :caption: Table of Contents
   :depth: 2
   :local:

Summary
-------

This design proposes a validated, scalable, and secure rail transportation network architecture tailored for metro/rail systems. The backbone uses a resilient **fiber ring topology** leveraging **SPB (Shortest Path Bridging, IEEE 802.1aq/IS-IS)** and/or **MPLS** for deterministic failover and service separation. Each station (a ring “cluster”) implements a **two-tier topology (Aggregation + Access)** to support Passenger Information System (PIS), Public Address (PA), CCTV, AFC/Ticketing, Telephony, Wi-Fi, Building Management (BMS), and Operations & Maintenance (O&M). Central Operations Control Center (OCC) and Backup Control Center (BOCC) connect redundantly to the ring.

The design is driven by five principles: **availability, determinism, security, visibility, and operational simplicity**.

**Availability & Determinism**
  - Fast convergence on ring failures with ERP/SPB or MPLS FRR (<50ms), dual-homing of all station aggregation pairs, and ECMP across diverse fiber paths.
  - Hitless or near-hitless maintenance through ISSU-ready platforms and service-based rerouting.

**Security & Segmentation**
  - Zero Trust at the edge with identity-based policies; strict **macro-segmentation (VRFs)** for Safety-Critical (SCADA/Interlocking), Mission-Critical (PIS/PA/CCTV), and Non-Critical (Guest Wi-Fi) domains; **micro-segmentation** via ACLs/roles.

**Visibility & Simplicity**
  - Single-pane-of-glass (OmniVista) for LAN/WLAN, AIOps analytics, topology, and compliance.
  - Centralized visibility and control via OmniVista for LAN, WLAN, and user policies—reducing IT effort and human error.
  - Plug-and-play onboarding of switches and access points with automated configuration templates, minimizing deployment time and ensuring configuration consistency.


Design Objectives
-----------------

Reliability and High Availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Target sub-second service protection on any single fiber cut or node failure on the ring.
- Redundant fiber pairs (clockwise/counter-clockwise), dual power feeds, and dual control centers (OCC/BOCC).
- Station-tier redundancy using dual aggregation switches (A/B) with multi-homed access.

Deterministic Performance & QoS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- End-to-end QoS model prioritizing **Safety-Critical** (Class 1), **Mission-Critical** (Class 2), and **Business/Best Effort** (Class 3).
- Bandwidth headroom on ring links (e.g., 2×25/100G) and 10G to stations for CCTV bursts and event traffic.

Security and Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Strong separation among SCADA/Signalling, Station Ops (PIS/PA/CCTV), Enterprise IT, and Guest using VRF/L2VPN constructs.
- 802.1X/MAB for edge ports, device profiling for IoT/OT, DHCP Snooping/DAI, MACsec/TrustSec (where supported) on fiber uplinks.

Manageability and Operational Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Standards-based telemetry (SNMP, Syslog, sFlow/NetFlow), event correlation, and automated compliance checks.
- ZTP for new stations/cabinets; golden templates, role-based policies, and change control workflows.

Resilience and Disaster Recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- OCC/BOCC active/standby services, replicated NMS and authentication & shared (DHCP/DNS) systems.
- Configuration/version archives and procedure playbooks for rapid restoration.

Regulatory & Environment
~~~~~~~~~~~~~~~~~~~~~~~~
- Industrial/ruggedized hardware for trackside cabinets (temp/EMC), locked-down ports, conformal coating options.
- Alignment with railway cybersecurity guidance and safety segregation practices (information only; operator policies prevail).

Proposed Network Architecture
-----------------------------

High Level Design - Transportation (Rail)
-----------------------------------------

.. figure:: images/station_design.png
   :alt: High Level Design - Transportation (Rail)
   :align: center
   :width: 70%

Core Architectural Principles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ring Core with ERP / SPB /MPLS
^^^^^^^^^^^^^^^^^^^^^^^
- **ERP Core**: ERP protocol control plane provides loop-free ring topology, per-service vlan, and fast convergence ERP. Ideal for IP/VLAN services between stations and OCC.
- **SPB Core**: IS-IS control plane provides loop-free multipath, per-service trees, and fast convergence without STP. Ideal for L2VPN services (MAC-in-MAC/802.1ah) between stations and OCC.
- **MPLS Core** (optional/adjacent): L2VPN (VPLS/EVPN) or L3VPN for inter-domain separation; **TI-LFA/FRR** for sub-50 ms protection. Useful for interop with IP/MPLS WAN or third-party backhaul.
- Dual counter-rotating fibers; diverse splice points; automatic traffic re-optimization after restoration.

Station Two-Tier (Aggregation + Access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Aggregation Tier**: Two redundant aggregation switches per station (AGG-A/AGG-B) form the station’s gateway into the ring. Each is uplinked to different ring directions and to different core nodes when feasible. Run SPB/MPLS-facing interfaces on the ring side, and VRF/service interfaces on the station side.
- **Access Tier**: Multiple access switches per subsystem (CCTV racks, PIS/PA racks, AFC rooms, concourse, platforms). Dual-homed via **MC-LAG/VC** to AGG-A/B; PoE/Hi-PoE for cameras, intercoms, Wi-Fi 6/6E APs. RSTP/MSTP stays in guard mode only (BPDU Guard, Loop Guard); primary forwarding via LAGs.

Data Centers / OCC & BOCC
^^^^^^^^^^^^^^^^^^^^^^^^^
- Redundant core/distribution pairs hosting service gateways, servers (PIS/PA controllers, VMS, recording), cybersecurity tools, and NMS. Fabric interconnect via SPB/MPLS.
- East–west traffic within data centers handled by EVPN-VXLAN or SPB; north–south pinned to ring core.

Services & Segmentation Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Macro Segmentation (VRFs / Service Instances)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **VRF-SCADA**: interlocking, traction power, environmental control networks (very restricted; one-way data diode options if applicable).
- **VRF-OPS**: PIS, PA, CCTV/VMS, emergency help points, telephony.
- **VRF-IT**: corporate IT, ticketing back-office, maintenance laptops.
- **VRF-GUEST**: guest Wi-Fi and public internet breakout (local or centralized).

Service Delivery Mechanisms
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **VLAN** per service for L2 extension where needed (e.g., CCTV VLAN between station and central VMS).
- **SPB I-SID** per service for L2 extension where needed (e.g., CCTV VLAN between station and central VMS).
- **MPLS L2/L3VPN** per tenant/service for deterministic isolation across third-party segments.
- **Inter-VRF** flows via firewalls or policy gateways with explicit allowlists (default-deny).

High Availability and Convergence Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Failure Domains**: Constrain faults to station or ring segment; avoid single points in power, fiber, or equipment.
- **Fast Detection**: BFD/CFM on core links; UDLD on fiber; sub-50 ms switchover with SPB tree recalculation or MPLS FRR.
- **Maintenance**: ISSU/GR where supported; drain services using per-service operations (I-SID/LSP level) before reloads.

Timing & Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~
- PTP grandmasters at OCC/BOCC; boundary/transparent clocks in aggregation. Profiles applied per-VRF where required; NTP as secondary.
- Time distribution monitoring and alarms upon asymmetry/drift.

Wireless LAN Design (Stations & Depots)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access Points (APs)
^^^^^^^^^^^^^^^^^^
- Ruggedized/indoor APs with Wi-Fi 6/6E/7. PoE+/Hi-PoE from access switches; plenum-rated or IP-rated where needed.

Architecture
^^^^^^^^^^^^
- Controllerless Stellar architecture with on-premises management (guest onboarding, analytics).
- Separate SSIDs mapped to VRFs (Staff/Operations, Maintenance, Guest).

RF/Operations
^^^^^^^^^^^^^
- DRM for channel/power; 20/40 MHz in dense platform/concourse areas; 80 MHz in low-density rooms.
- 802.11k/r/v for roaming; sticky client avoidance; minimum RSSI enforcement.

Core Ring Design 
---------------------------------
- Two **Core** switches/Router (rack 1 & rack 2), each with:
  - 2×25/40/50/100G attachment to the ring (opposite ring directions (diverse ducts)).
  - Dual AC/DC power; separate UPS circuits; external dry-contact alarms to BMS.

Logical Topology & Control Planes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Ring Core**: ERP Ring with IP/VLAN per service; SPB (IS-IS) with I-SIDs per service; or MPLS with LDP/SR and L2/L3VPNs.


Station Network Design 
---------------------------------

Physical Topology per Station
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Two **Aggregation** switches (rack 1 & rack 2), each with:
  - 2×10/25/40/50/100G uplinks to Core Switch/Router.
  - 2×10/25G downlinks (MC-LAG) to each Access switch block.
  - Dual AC/DC power; separate UPS circuits; external dry-contact alarms to BMS.
- **Access** blocks by subsystem:
  - **CCTV**: Hi-PoE for PTZs; local SSD/NVR cache optional; multicast suppression enabled.
  - **PIS/PA**: audio controllers, displays; multicast (PIM-SM/SSM) only within VRF-OPS.
  - **AFC/Ticketing**: secure VLANs; PCI-DSS-aligned segmentation where applicable.
  - **O&M**: maintenance jacks with NAC posture checks; jump host model.
  - **Wi-Fi APs**: dual-band, dual-radio.

Logical Topology & Control Planes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Station Aggregation**: IP/VLAN/VRF per service; SPB (IS-IS) with I-SIDs per service;
- **Station Edge**: VLAN with MVRP mapped to VRF or ISID service.
- **RSTP** in primary forwarding paths; protection features only.

Trackside Network Design
---------------------------------

The trackside network extends the core ERP/SPB/MPLS ring to wayside environments, enabling
mission-critical communication for signalling, safety systems, surveillance, and
operational maintenance. It supports both **CBTC and ETCS** signalling models through
strict segregation of safety-related and non-safety services.

Trackside Fiber Topology & Redundancy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Dual fiber routes aligned with track alignment (up-line / down-line or bi-directional).
- Integration with station aggregation via geographically diverse entries.
- Passive optical joints and splice enclosures installed at regular intervals with OTDR
  test points for break detection and maintenance.
- Fast reroute (ERP / SPB or MPLS-FRR) ensures sub-second convergence upon track cut or equipment loss.

Wayside Cabinets & Industrial Switching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Industrial EN50155/IEC61850-grade switches housed in trackside or tunnel cabinets.
- Each cabinet includes:
  - ERPSPB/MPLS uplinks to track fiber pair.
  - PoE/Hi-PoE downlinks for field devices (CCTV, PA, Signal I/O, Emergency Phones).
  - Dual DC power feeds (typically -48V DC) with local breaker isolation.
- Cabinets are environmentally rated (IP54–IP66) to withstand temperature, humidity,
  vibration, and EMC exposure typical of tunnel/viaduct conditions.

Signalling System Integration (CBTC/ETCS Safe Zones)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Dedicated **Safety-Critical VRF or I-SID** reserved for signalling/CBTC/ETCS backhaul.
- One-way data flow options supported through external firewalls or data diodes if mandated.
- Integration with signalling Zone Controllers or Trackside Processing Units via secure
  Layer 2/Layer 3 circuits, with latency and jitter guarantees.
- Field I/O controllers connected via rugged access switches using static addressing and
  ACL-based micro-segmentation.

Trackside CCTV, PA, and Emergency Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Trackside CCTV poles or tunnel cameras connected via Hi-PoE ports; multicast suppression
  and IGMP snooping enabled to protect backhaul capacity.
- Emergency Help Points (EHPs) and trackside telephony placed at evacuation walkways or portals.
- PA/voice evacuation horns or tunnel loudspeakers linked to station PA controllers via
  VRF-OPS or VRF-PUBLIC address spaces.

Trackside Wireless (Maintenance Wi-Fi / Trainborne Access)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Optional Wi-Fi access points (ruggedized, 5/6 GHz) mounted at portals, crossover areas,
  or depots to support maintenance teams and rolling stock diagnostics.
- SSIDs segregated by VRF (Maintenance / Guest / Trainborne Service).
- Alignment for future CBTC wireless bearer (e.g., 5.8 GHz track-to-train) if deployed.

Environmental Hardening & Power
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- All trackside equipment designed for harsh environments:
  - Operating Temp: –25°C to +70°C (fanless preferred).
  - Vibration/Shock: IEC 60068-2.
  - EMC Immunity: EN 50121-4 (railway signalling immunity).
- Power redundancy via dual DC feed or local UPS buffer within wayside cabinets.
- Fiber connectors protected with sealed glands and color-coded for route identification.

Security Architecture and Zero Trust Controls
---------------------------------------------

Identity & Admission
~~~~~~~~~~~~~~~~~~~~
- 802.1X EAP-TLS for IT/Staff; **MAB/Certificates/PSK** for OT endpoints; device fingerprinting maps to roles.
- Dynamic VLAN/VRF assignment via **User/Device Network Profiles (UNP)** at edge (switch/AP).

Edge & Transport Protections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- DHCP Snooping, DAI, IP Source Guard; storm control and rate limiting on broadcast/multicast.
- **MACsec** or link encryption on fiber inter-station links where required.
- Default-deny inter-VRF; firewall inspection for north–south flows to servers or internet.

Threat Monitoring & Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- WIPS on selected AP models for rogue detection; NetFlow/sFlow export to SIEM; syslog to SOC with tamper-evident storage.
- Command logging, TACACS+/RADIUS with MFA; RBAC for NOC/SOC/Field Ops.

IoT/OT Onboarding & Containment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Template-based onboarding for CCTV, PIS, PA, AFC; per-device rate limits and ACLs.
- East–west containment using micro-ACLs at access edge and inter-VRF firewalls at aggregation.

QoS and Traffic Engineering
---------------------------

Classes & Prioritization
~~~~~~~~~~~~~~~~~~~~~~~~
- **Class 1 – Safety-Critical**: signalling/SCADA telemetry; DSCP EF/CS6; strict priority queues; jitter <10 ms.
- **Class 2 – Mission-Critical**: PA/PIS control, VMS control, voice; AF41/EF as applicable; WRR with high weight.
- **Class 3 – High-Bandwidth**: CCTV video; AF31/AF32 with policing to protect Class 1/2.
- **Class 4 – Business/Best Effort**: office IT, guest internet; BE/AF11; shaped per-user/SSID.

Mechanics
~~~~~~~~~
- Trust DSCP from known sources (controllers, servers); remark at edge for others.
- Multicast scoping for PA/PIS; IGMPv3/SSM within VRF-OPS; PIM-SM rendezvous at station aggregation or OCC.
- ECMP across ring paths; per-service load sharing (SPB I-SID trees or MPLS ECMP).

Management and Automation Framework
-----------------------------------

Unified Management & AIOps
~~~~~~~~~~~~~~~~~~~~~~~~~~
- OmniVista for inventory, config, firmware, topology, and analytics.
- Health scores for stations, cameras, APs; drift detection and intent compliance.

Provisioning & Templates
~~~~~~~~~~~~~~~~~~~~~~~~
- **ZTP** for new switches/APs; role-based templates (AGG, ACC-CCTV, ACC-PIS/PA, ACC-AFC, ACC-O&M).
- Fabric auto-attach (iFab) to extend services/I-SIDs to the correct access ports based on LLDP fingerprints.

Telemetry & Compliance
~~~~~~~~~~~~~~~~~~~~~~
- SNMPv3, secure syslog, and flow export; log retention aligned with operator policy.
- Nightly backups; signed configs; software image pinning; staged rollouts per station group.

Resilience, Power, and Environmental Considerations
---------------------------------------------------
- Dual PSU per switch; separate UPS feeds; -48V DC where required in trackside cabinets.
- Fan/filter maintenance windows coordinated with off-peak hours.
- Fiber plant with OTDR baselines; spare cores reserved; labeled and documented patch maps.

Model Selection Matrix (Deployment Zone vs Technology)
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 25 25

   * - 
     - **ERP**
     - **SPB**
     - **MPLS**

   * - **Scalability**
     - 32 nodes ring  
     - Large scale with 
       
       sub-second convergence 
     - Large scale with 
     
       50ms convergence

   * - **Core / Backbone**
     - OS6900 / OS68xx      
     - OS9900 / OS6900 
     - Nokia SR Router

   * - **Station Aggregation**
     - OS6900 / OS68xx  
     - OS6900 / OS68xx
     - OS6900 / OS68xx

   * - **Station Access**  
     - OS68xx / OS6560  
     - OS68xx / OS6560
     - OS68xx / OS6560

   * - **Trackside / Wayside**
     - OS6865 / OS6465  
     - OS6865 / OS6465
     - OS6865 / OS6465

   * - **Data Center / OCC**
     - OS6900 / OS68xx / OS6560
     - OS6900 / OS68xx
     - OS6900 / OS68xx

   * - **Wireless (Wi-Fi APs)**
     - OAW-AP15xx (Indoor) / 
       
       OAW-AP136x (Outdoor) / 
       
       OAW-AP157x (Outdoor)  
     - OAW-AP15xx (Indoor) / 
       
       OAW-AP136x (Outdoor) / 
       
       OAW-AP157x (Outdoor)  
     - OAW-AP15xx (Indoor) / 
       
       OAW-AP136x (Outdoor) / 
       
       OAW-AP157x (Outdoor)  

   * - **Wireless Mgmt / NAC**
     - OmniVista 2500/
       
       OmniVista Terra  
     - OmniVista 2500/
       
       OmniVista Terra
     - Nokia NFM and 
       
       OmniVista 2500/
       
       OmniVista Terra

