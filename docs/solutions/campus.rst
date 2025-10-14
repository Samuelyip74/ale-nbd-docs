Campus/Enterprise Network Design (Wired & Wireless)
=============================================================

.. contents::
   :caption: Table of Contents
   :depth: 2
   :local:

Summary
--------------------

This design proposes a validated, scalable, and secure campus network architecture for wired and wireless access using Alcatel-Lucent Enterprise (ALE) OmniSwitch LAN, OmniAccess Stellar WLAN, and OmniVista Management.
The design adopted three key principles: performance, security, and operational simplicity.

**Performance**

To deliver a high-quality user experience across both wired and wireless infrastructure, the design emphasizes:

  **High Availability & Redundancy**
    Use of resilient network topologies such as OSPF (Open Shortest Path First), and Virtual Chassis ensures non-stop forwarding, rapid convergence, and network continuity.

  **Optimized Traffic Flow & Low Latency**
    Traffic engineering supports equal-cost multipathing (ECMP) and intelligent load balancing across multiple links, reducing congestion and ensuring stable performance for critical applications such as voice, video collaboration, and real-time mobility services.

  **Scalable Throughput for Growth**
    Architecture supports seamless scalability—from small deployments to large multi-building campuses—accommodating future expansion in users, IoT devices, and application demands without redesign.

**Security**

Security is integrated from the edge to the core, protecting users, devices, and data throughout the campus:

  **Unified Access Control (Wired & Wireless)**
    Enforcement of BYOD, corporate, and guest policies through OmniAccess Stellar WLAN and OmniSwitch Access Guardian, using 802.1X, MAC authentication, and dynamic VLAN assignment.

  **Network Micro-Segmentation & User Isolation**
    Use of virtualized services (VRF) to isolate departments, critical systems, and IoT endpoints, preventing lateral movement and containing potential threats.

  **Advanced Threat Detection & Compliance**
    Integration with OmniVista Cirrus or OmniVista Network Advisor for real-time analytics, rogue AP detection, dynamic quarantine, and automated remediation, aligning with Zero Trust security principles.

**Operational Simplicity**

Designed to reduce complexity in deployment, configuration, and ongoing management:

  **Single-Pane-of-Glass Management**
    Centralized visibility and control via OmniVista for LAN, WLAN, and user policies—reducing IT effort and human error.

  **Automation & Zero-Touch Provisioning (ZTP)**
    Plug-and-play onboarding of switches and access points with automated configuration templates, minimizing deployment time and ensuring configuration consistency.

  **Consistent Policy and Fabric Integration**
    Fabric auto-attach (iFab) with EVPN-VXLAN/OSPF underlay and unified user profiles allows consistent policy enforcement across wired and wireless environments without complex manual VLAN stitching.


.. _design_objectives:

Design Objectives
-----------------

The campus network design aims to provide a robust, scalable, and secure infrastructure
that supports current operational needs while accommodating future growth. The following
key objectives guide the overall architecture and implementation.

Reliability and High Availability
---------------------------------
- Ensure continuous network operation with minimal downtime.
- Implement redundancy at core, distribution, and access layers
  (e.g., dual core switches, link aggregation, redundant uplinks).
- Enable rapid failover and fast convergence using technologies such as STP, VRRP,
  and dynamic routing protocols (e.g., OSPF, BGP).

Scalability and Future Growth
-----------------------------
- Adopt a modular, hierarchical design (Core–Distribution–Access) to support expansion.
- Allow seamless integration of additional buildings, departments, or services.
- Design for high user density and increasing device connectivity (wired and wireless).

Performance and Optimized Traffic Flow
--------------------------------------
- Deliver high bandwidth and low latency for critical applications such as voice, video, and data.
- Use Quality of Service (QoS) to prioritize business-critical and real-time services.
- Prevent bottlenecks through link aggregation, load balancing, and adequate uplink capacity.

Security and Access Control
---------------------------
- Enforce network segmentation using VLANs, ACLs, and routing policies.
- Implement identity-based access control (802.1X, NAC) for user and device authentication.
- Protect against threats using perimeter firewalls, IDS/IPS, and continuous monitoring.

Manageability and Operational Efficiency
----------------------------------------
- Standardize configurations, naming conventions, and documentation.
- Provide centralized network management for monitoring (SNMP, Syslog, NetFlow) and automation.
- Support regular backup, configuration versioning, and software maintenance procedures.

Resilience and Disaster Recovery
-------------------------------
- Include backup paths and redundant services for core functions (DNS, DHCP, authentication).
- Document recovery procedures for hardware, link, or power failures.
- Ensure the network design supports business continuity requirements.

User Experience and Service Quality
-----------------------------------
- Guarantee consistent performance across academic, administrative, and public spaces.
- Deliver reliable wireless coverage with seamless roaming across the campus.
- Support mobility, BYOD, IoT, VoIP, video conferencing, and collaboration platforms.

Compliance and Policy Alignment
-------------------------------
- Align with institutional IT governance and industry standards (ISO, GDPR, HIPAA if applicable).
- Ensure compliance with data protection, audit, and access control requirements.
- Provide traceability and logging for security and operational audits.

Energy Efficiency and Sustainability
------------------------------------
- Use energy-efficient devices and intelligent power management.
- Optimize cooling and rack space in network facilities.
- Promote long-term sustainability by planning lifecycle replacement and hardware recycling.

Proposed Network Architecture
------------------------------------

The proposed campus network architecture is designed to fulfil the key design objectives
of high availability, scalability, performance, security, and operational efficiency.
It integrates modern data center technologies with resilient campus infrastructure to
deliver a unified, future-ready network platform.

Core Architectural Principles
-----------------------------

EVPN-VXLAN Fabric for Virtualization and Mobility
   Utilizes an EVPN-VXLAN overlay fabric to provide scalable Layer 2 and Layer 3
   virtualization. This enables seamless host mobility, tenant separation, and
   efficient east–west traffic handling within data center and campus environments.
   The fabric supports multi-tenancy and simplifies large-scale segmentation.

High-Performance and Resilient Core/Distribution
   The campus core and distribution layers are built with high availability in mind,
   using redundant routing paths, fast convergence protocols (e.g., OSPF, BGP),
   and link aggregation. The design minimizes single points of failure and ensures
   consistent service continuity during component failures or maintenance events.

Multi-Gigabit Wired Access with PoE/Hi-PoE
   Access switches provide multi-rate interfaces (1/2.5/5/10 Gbps) to support modern
   high-bandwidth endpoints such as Wi-Fi 6/6E access points, surveillance systems,
   and IoT devices. Power over Ethernet (PoE+/Hi-PoE) ensures simplified device
   deployment and centralized power control.

Optimized Wireless with Dynamic Radio Management (DRM)
   Wireless infrastructure incorporates Dynamic Radio Management to automatically
   optimize channel selection, transmit power, and load balancing. This ensures
   reliable performance in high-density areas such as lecture halls, auditoriums,
   offices, and public zones.

Zero Trust Security with Macro and Micro Segmentation
   Security is enforced through both macro-segmentation (VRFs, VLANs) and
   micro-segmentation (policy-based access control). This Zero Trust approach ensures
   that users and devices are authenticated, authorized, and monitored, regardless of
   physical location on the network.

Unified Management and Automation
   Centralized orchestration and visibility are provided by OmniVista Cirrus and
   OmniVista Network Advisor. These platforms enable automated provisioning, AI-driven
   analytics, fault diagnostics, configuration compliance, and lifecycle management—
   reducing operational overhead and improving service delivery.

Campus Core and Distribution Fabric Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The core and distribution layers form the operational backbone of the campus network.
This design prioritizes high availability, deterministic performance, and fast
convergence to ensure uninterrupted service delivery during failures, upgrades, or
traffic surges. A fabric-based architecture is implemented to simplify L2/L3 services,
support segmentation, and provide consistent connectivity across buildings and data centers.

**Core and Distribution Switching**
   - Redundant OmniSwitch modular/core platforms (e.g., OS9900, OS6900, OS6870) deployed
     in pairs to eliminate single points of failure.
   - Devices operate as a virtual chassis to provide a single
     logical control plane with unified configuration and hitless failover.
   - High-speed 25/40/100G inter-switch links ensure ample backbone capacity for
     campus-wide east–west and north–south traffic.

**Data Center Integration (Spine-Leaf Fabric)**
   - Dedicated data center fabric built using spine–leaf topology on OmniSwitch
     platforms, leveraging EVPN-VXLAN for scalable network virtualization.
   - Seamless integration between campus fabric and data center fabric enables
     consistent multi-tenant VLAN extension, workload mobility, and DR readiness.

**Access Layer Uplinks and Multihoming**
   - Access switches (OS6560, OS6570M, OS6860, OS6870 series) are dual-homed to the
     distribution/core layer using Link Aggregation Control Protocol (LACP) in
     Multi-Chassis Link Aggregation (MLAG) or Virtual Chassis (VC) mode. This provides
     redundant uplinks, eliminates single points of failure, and avoids dependency on
     legacy spanning tree mechanisms for primary path selection.
   - Multi-gigabit interfaces (1/2.5/5/10G) with PoE+/Hi-PoE support deliver scalable
     edge connectivity for high-density endpoints such as access points, security
     cameras, IoT sensors, and AV infrastructure.
   - VLAN propagation and configuration consistency across the access layer are
     automated using Multiple VLAN Registration Protocol (MVRP), reducing manual
     provisioning effort and preventing VLAN mismatch or orphaned segments.
   - Spanning Tree Protocol (RSTP/MSTP) remains enabled in a protective role (loop guard,
     BPDU guard, root guard), while primary traffic forwarding is managed through
     LACP-based topologies to ensure deterministic routing and sub-second failover.

**Campus Routing and Multicast Services**
   - OSPF is implemented as the primary Interior Gateway Protocol (IGP) to provide
     dynamic routing, fast convergence, and scalable Layer 3 reachability across
     the campus backbone.
   - Equal-Cost Multi-Path (ECMP) routing is leveraged to distribute traffic across
     redundant links, ensuring deterministic load sharing and improved resiliency.
   - Multicast routing (PIM Sparse Mode or Source-Specific Multicast) supports
     real-time applications such as IPTV, digital signage, emergency broadcast
     systems, and campus-wide live streaming.
   - Logical segmentation is achieved using VLANs and VRFs, enabling separation of
     administrative, academic, guest, and operations services without reliance on
     complex legacy tunneling or proprietary protocols.

**High Availability and Convergence Strategy**
   - Sub-second failover through fast link detection, BFD, and topology-independent
     loop-free routing ensures traffic continuity.
   - ISSU (In-Service Software Upgrade)
     capabilities allow maintenance activities without service interruption.
   - End-to-end redundancy (dual fabrics, dual uplinks, redundant power/PSUs) supports
     mission-critical applications and essential campus services.

Wireless LAN Design
~~~~~~~~~~~~~~~~~~~

The wireless LAN is designed to deliver consistent high-performance connectivity across
the campus, with specific attention to high-density environments such as lecture theatres,
auditoriums, laboratories, student hubs, and open collaboration areas. The architecture
leverages Dynamic Radio Management (DRM) and advanced RF planning to ensure optimal
coverage, capacity, and user experience.

**Access Points (APs)**
   - OmniAccess Stellar latest-generation Wi-Fi 6/6E/7-capable access points.
   - Dual or tri-radio models to support simultaneous 2.4 GHz, 5 GHz, and 6 GHz bands.
   - Support for OFDMA, MU-MIMO, and BSS Coloring to enhance multi-user performance.

**Architecture**
   - Distributed, controllerless architecture where APs coordinate autonomously,
     eliminating single points of failure associated with centralized controllers.
   - Cloud augmentation via OmniVista Cirrus for global policy management, AI-driven
     insights, guest onboarding, and firmware lifecycle automation.

**Dynamic Radio Management (DRM)**
   - Automatic channel selection and transmit power adjustment to minimize interference.
   - Intelligent band steering to direct capable clients to 5 GHz/6 GHz for improved throughput.
   - Real-time load balancing between APs to prevent congestion during peak usage (e.g., exams, events).
   - Automatic detection and mitigation of rogue APs and non-Wi-Fi interference sources.

**RF Planning and Spectrum Strategy**
   - 5 GHz and 6 GHz as primary bands for high-capacity traffic; 2.4 GHz retained for legacy/IoT devices.
   - DFS channel awareness and pre-assigned channel plans to prevent radar interference.
   - Channel width planning: 20/40 MHz default in dense areas; 80/160 MHz used selectively in low-density zones.
   - Coverage design based on -65 dBm primary signal and secondary AP overlap for seamless roaming.

**SSID and Access Segmentation**
   - Corporate SSID secured using 802.1X/EAP with integration to RADIUS / NAC.
   - Guest SSID using captive portal with bandwidth and time-based policies.
   - IoT/Operations SSID using MAC-based authentication or Unified Profile policies (UNP).
   - Client isolation and L2/L3 segmentation aligned with Zero Trust and micro-segmentation principles.

**High-Density and User Experience Enhancements**
   - Minimum RSSI enforcement to prevent low-quality client associations.
   - Sticky client avoidance via intelligent roaming thresholds and 802.11k/r/v support.
   - Application Visibility and QoS for prioritizing real-time services (VoIP, collaboration, LMS tools).

Management and Automation Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The network management and automation strategy is designed to ensure operational
efficiency, proactive monitoring, and consistent policy enforcement across the entire
campus fabric. Centralized tools and automation workflows reduce configuration errors,
accelerate deployment, and support AI-assisted troubleshooting and lifecycle management.

**Unified Management Platform**
   - OmniVista Cirrus (SaaS) provides a single pane of glass for wired and wireless
     infrastructure, offering centralized configuration, firmware lifecycle management,
     topology visualization, inventory tracking, and alarm correlation.
   - Role-based access control (RBAC) enables secure delegation of operational tasks to
     network, security, and service desk teams.

**Deployment Automation and Provisioning**
   - Zero-Touch Provisioning (ZTP) enables automatic onboarding of new switches and
     access points upon connection to the network, applying predefined configuration
     profiles without manual intervention.
   - Intelligent Fabric (iFab) and auto-attach mechanisms dynamically extend VLANs and
     fabric services based on device roles or LLDP discovery, minimizing provisioning
     time and preventing misconfiguration.
   - Configuration templates enforce standards for naming, VLAN allocation, QoS policies,
     and security parameters across all network domains.

**AI-Driven Operations (AIOps)**
   - OmniVista Network Advisor applies machine learning for anomaly detection, drift
     identification, and predictive insight into bandwidth, client density, and hardware
     health.
   - Automated root-cause guidance assists operations teams in remediating issues
     such as RF interference, link flaps, or authentication failures.
   - Capacity and trend analytics provide actionable insights for capacity planning,
     Wi-Fi optimization, and hardware refresh strategy.

Security Architecture and Zero Trust Controls
---------------------------------------------

The security architecture follows a Zero Trust model, where identity, device posture,
and policy enforcement are applied at every access point. Security is integrated into
the switching, wireless, and management layers to ensure continuous protection against
lateral movement, rogue devices, and credential-based threats.

Security Controls (Zero Trust Approach)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Identity and Posture Enforcement**
   - 802.1X with EAP-TLS for corporate users leveraging certificate-based authentication.
   - MAC Authentication Bypass (MAB) and Per-Device PSK for non-supplicant devices
     such as IoT, medical, and OT endpoints.
   - Device posture validation via NAC integration (e.g., OmniVista NAC, ClearPass,
     or Microsoft Entra Conditional Access).

- **Edge Policy Enforcement**
   - User Network Profiles (UNP) map authenticated identities to their VLAN/VRF, ACL,
     and QoS policies at the first point of entry (switch/AP).
   - Default-deny inter-zone traffic with explicit allowlists per application or service.
   - Prevention of lateral movement through edge ACLs and per-role traffic segmentation.

- **Threat Monitoring and Telemetry**
   - Dedicated scanning radios (WIPS) on Stellar AP models for rogue AP detection,
     Evil Twin attacks, and Wi-Fi intrusion prevention.
   - NetFlow/sFlow export to SIEM or security analytics platforms for traffic anomaly
     detection and behavior analytics.
   - Syslog integration with Security Operations Centers (SOC) for event correlation,
     compliance logging, and audit readiness.

- **Privileged Access Protection**
   - Administrator authentication via RADIUS/TACACS+ with enforced MFA (e.g., Microsoft Entra ID).
   - Role-Based Access Control (RBAC) in OmniVista to restrict configuration access
     by job function (e.g., network ops vs. security admin).
   - Command logging and session tracking for compliance and forensic audits.

Identity & Segmentation
~~~~~~~~~~~~~~~~~~~~~~~~
- **UNP-Based Segmentation**
   - User/Device Network Profiles deliver identity-driven access, dynamically assigning
     VLAN, VRF, ACL, and QoS policies based on role, posture, or device classification.
   - Supports containerized segmentation for Corporate, Guest, IoT, and OT zones.

- **Micro-Segmentation**
   - Fine-grained segmentation at the edge (switch/AP) isolates traffic between
     device groups or application tiers.
   - Dynamic enforcement using ACLs, VRFs, and virtual containers without traditional
     VLAN sprawl or firewall bottlenecks.

- **Guest Access Integration**
   - Microsoft Entra ID and social media (Google, Facebook, LinkedIn) authentication
     supported for guest onboarding via captive portal.
   - Time- and bandwidth-limited access profiles, with optional sponsor approval
     or email/SMS verification.

IoT/OT Onboarding and Fingerprinting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Discovery and Classification**
   - Device fingerprinting using OmniVista’s cloud signature database to identify
     device type, manufacturer, and OS.
   - Device categories automatically mapped to corresponding UNP/role containers
     (e.g., CCTV, HVAC, POS systems).

- **Dynamic Policy Assignment**
   - Category-based UNP enforcement places devices into correct VLAN/VRF with
     appropriate ACL and QoS policies without manual intervention.
   - Integration with DHCP-Snooping and ARP Inspection to prevent spoofing.

- **Hardening and Policy Containment**
   - Per-device PSK or certificate-based onboarding for high-risk OT environments.
   - East–West containment using edge ACLs, inter-VRF firewalls, and rate-limiting.
   - Enforcement of infrastructure protections such as BPDU Guard, Storm Control,
     and Source-Guard at the access layer.

QoS and Traffic Engineering
------------------------------------

The Quality of Service (QoS) and traffic engineering strategy ensures consistent
application performance across the campus, prioritizing real-time services such as
voice, video, and collaboration, while controlling bandwidth usage from guest and
non-critical devices. Policies are enforced from the access layer to the core,
maintaining an end-to-end differentiated service model aligned with enterprise SLAs.

**Traffic Classification and Marking**
   - Wireless traffic is classified at the point of entry using 802.11e/WMM profiles,
     mapping SSID profiles and application types to DSCP values.
   - Edge switches are configured to trust incoming CoS/DSCP markings from APs and
     apply remarking where necessary to maintain class integrity.
   - Application recognition (L7 DPI where supported) is used to identify collaboration
     platforms (e.g., Teams, Zoom), VoIP services, and critical enterprise applications.

**Queuing and Scheduling**
   - Strict Priority Queues are dedicated for Expedited Forwarding (EF) traffic such as
     VoIP signalling and real-time audio streams to ensure minimal latency and jitter.
   - Assured Forwarding classes (AF41/AF42) are reserved for video conferencing and
     high-priority collaboration traffic, using Weighted Round Robin (WRR) scheduling.
   - Default best-effort queues handle data applications, with congestion management
     algorithms preventing starvation of low-priority flows.

**Rate-Limiting and Traffic Shaping**
   - Per-SSID and per-user bandwidth policies are applied to guest and IoT networks to
     prevent non-critical traffic from impacting corporate services.
   - Policing and shaping profiles enforce maximum throughput limits and burst controls
     during congestion periods.
   - Multicast and broadcast traffic rate controls are implemented to safeguard campus
     control plane stability and protect wireless airtime.

**End-to-End QoS Policy Alignment**
   - QoS markings are preserved across routing and switching hops to ensure consistent
     treatment through the core and data center paths.
   - Integration with WAN/SIP edge gateways ensures that QoS policies extend beyond
     the campus for unified service quality across cloud and remote access environments.
   - Compliance with industry models (DiffServ, RFC 4594) ensures interoperability with
     carrier networks and hosted collaboration platforms.
