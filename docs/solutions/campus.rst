
Campus/Enterprise Network Design (Wired & Wireless)
=============================================================

.. contents:: Table of Contents
   :depth: 2
   :local:

Summary
--------------------

This design targets a campus environment with a classic Core/Distribution model integrated with an EVPN-VXLAN fabric extension for data center interconnect. The architecture enforces Zero Trust principles with NAC/Firewall integration and strict Guest & IoT isolation.
This document proposes a validated, scalable, and secure campus network architecture for wired and wireless access using Alcatel-Lucent Enterprise (ALE) OmniSwitch LAN, OmniAccess Stellar WLAN, and OmniVista management. The design supports Digital Age Networking (automation-first operations), zero-trust segmentation, and Wi-Fi 7 readiness with multi-gigabit edge.

Technical Requirements
------------------------------------

- **User & device scale:** <X> concurrent users, <Y> IoT/OT endpoints, growth <Z>%/year
- **Sites:** HQ + <N> branches, <M> buildings, <F> floors each
- **Applications:** Unified comms/voice, video collaboration, ERP/CRM, VDI, SaaS, on-prem DC, guest Wi-Fi
- **Security posture:** Zero trust by default; identity-based segmentation; least-privilege access
- **Availability:** Campus core HA, access redundancy where critical. Target SLA: <e.g., 99.95%>
- **Performance:** Per-user throughput targets, Wi-Fi 7 multi-gig (>1/2.5/5/10 Gbps) uplinks, low latency for real-time apps
- **Operations:** Unified Management, API/automation, AIOps with anomaly detection
- **Sustainability & TCO:** High-efficiency PoE, lifecycle automation, Opex-friendly subscription option

Reference Architecture
-------------------------

This architecture now incorporates:

- **EVPN-VXLAN campus fabric** for scalable L2/L3 virtualization and seamless mobility.
- **Dynamic Radio Management (DRM)**, to provide optimized Wi-Fi performance in high-density environments.
- **Macro & Micro Segmentation** aligned with Zero Trust Architecture.
- **Zero Trust Enforcement Flow using UPAM (OmniVista Built-In NAC) → OmniSwitch/Stellar → Palo Alto NGFW**

Campus Fabric
~~~~~~~~~~~~~~~~~

- **Core/Distribution:** Redundant OmniSwitch modular/core (e.g., OS9900/OS6900/OS6870) forming the campus fabric.
- **Data Center:** Redundant OmniSwitch modular/switch (e.g., OS9900/OS6900/OS6870) forming the Data Center fabric in spine-leaf topology.
- **Access:** OmniSwitch 6560/6570M/6860/6870 series at the edge with multi-gig (2.5/5/10G) ports and PoE+/Hi-PoE.
- **East-West & Simplified L2/L3:** Use SPB (Shortest Path Bridging) or equivalent campus fabric to simplify VLAN extension and L3 virtualization, delivering fast convergence and deterministic paths.
- **Uplinks:** Dual-homed access with MLAG/VC/IS-IS-SPB depending on platform; 25/40/100G core interconnects.

Wireless LAN
~~~~~~~~~~~~~~~~

- **APs:** OmniAccess Stellar (latest gen; Wi-Fi 6/6E/7-access points).
- **Architecture:** Distributed controllerless architecture (APs coordinate; eliminates controller SPoF) with cloud-augment via OmniVista Cirrus.
- **RF Design:** 5 GHz/6 GHz primary; 2.4 GHz legacy. DFS planning; channel width 20/40/80 (and 160/320 MHz for Wi-Fi 6E/7 where justified). 
   Separate SSIDs for Corp (802.1X), Guest (captive portal), and IoT (MAC/UNP workflows). Band steering and min-RSSI enforced.

Management & Automation
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Unified management:** OmniVista Cirrus (SaaS) for configuration, inventory, alarms, and analytics across LAN/WLAN.
- **Automation:** Zero-Touch Provisioning (ZTP), fabric auto-attach/Intelligent Fabric (iFab) profiles, config templates.
- **AIOps:** OmniVista Network Advisor for anomaly detection, root-cause hints, and capacity insights.

Identity & Segmentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **UNP (User/Device Network Profiles):** Identity-based access with role-mapped VLAN/VRF/ACL/QoS.
- **Micro-segmentation:** Containerized network “zones” for Corp/Guest/IoT/OT; dynamic policy enforcement at the edge (switch/AP) after fingerprinting & authentication.

Detailed Design
------------------

Wired Access
~~~~~~~~~~~~~~~~

- **Edge switches:** OS6560/6570M/6860/6870 with 1/2.5/5G access ports and 10G uplinks. PoE+ (30W) baseline; Hi-PoE (60–90/100W) where APs/cameras/IP Phone require it.
- **Cabling:** Cat6A for multi-gig + PoE++ runs up to 100 m; fiber SM/MM for uplinks. Ensure power budgets per IDF and thermal planning.
- **Access resiliency:** Dual uplinks to redundant distribution/fabric nodes; optional stack/VC at edge for simplified ops.

Wireless Access
~~~~~~~~~~~~~~~~~~~

- **Capacity planning:** Model clients/AP (busy hour), application mix (collab/video/AR), and SNR targets. Start with 25–35 clients per AP (enterprise office) and adjust for density areas (lecture halls, auditoria).
- **PoE & Uplink planning:** Ensure AP ports support 2.5/5/10G and PoE+/bt; IDFs sized for higher draw for Wi-Fi 7 radios and scanning radios.
- **Roaming:** 802.11k/v/r enabled; sticky-client mitigation via min-RSSI. For latency-sensitive voice, validate call-roam KPIs (<150 ms handoff where possible).
- **Guest & IoT:** Guest SSID via captive portal/VLAN to internet breakout; IoT SSID with MAC or PSK per-device and dynamic UNP role assignment.

Core/Distribution & Routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Fabric:** IP/OSPF at Core/Distribution; VRFs for Corp/Guest/IoT; summarized routing to WAN/SD-WAN.
- **DHCP/DNS:** Redundant services with IPAM integration; DHCP option-based IoT onboarding as needed.
- **Internet/WAN:** Dual ISPs; SD-WAN/SASE where applicable; QoS for UC.

Security Controls (Zero Trust Approach)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Identity & Posture:** 802.1X/EAP-TLS for users; MAB/PSK-per-device for non-supplicants; device posture via NAC integration.
- **Edge enforcement:** UNP-mapped ACL/QoS at switch/AP, preventing lateral movement. Default-deny between zones; allowlists per app.
- **Threat monitoring:** Dedicated scanning radios on AP models that support WIPS; NetFlow/sFlow export; syslog to SIEM.
- **Privileged access:** Admin RADIUS/TACACS+, MFA for management plane; RBAC in OmniVista.

IoT/OT Onboarding & Fingerprinting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Discovery & classification:** OmniVista device fingerprinting (cloud-signature DB) builds an inventory; map device categories to UNPs.
- **Dynamic policy:** Category-based UNP enforcement at the edge (switch/AP) to auto-place devices into correct containers/VRFs.
- **Hardening:** Per-device PSK or certs; restrict East-West; rate-limit, DHCP-snooping, ARP inspection where applicable.


Addressing Key Modern Drivers
--------------------------------

- **Wi-Fi 7 readiness:** Multi-link operation (MLO), 320-MHz channels in 6 GHz where regulatory/RF permits; ensure multi-gig edge and adequate PoE budgets.
- **Automation/DAN:** Accelerate service activation with fabric auto-attach and templates; reduce human error.
- **AI-assisted Ops:** Use AIOps insights to detect anomalies, capacity saturation, and noisy neighbors; enable intent-based drift checks.

6) IP Plan & VLAN/VRF Schema (example)
--------------------------------------

.. list-table:: IP Plan & VLAN/VRF Schema (example)
   :header-rows: 1
   :widths: 15 15 15 25 30

   * - Zone
     - VRF
     - VLANs
     - IP CIDR
     - Notes
   * - Corp Users
     - VRF-CORP
     - 100–150
     - 172.16.X.0/24 (per VLAN schema)
     - 802.1X; SGT/UNP role mapping
   * - Guests
     - VRF-GUEST
     - 200–209
     - 10.20.0.0/16
     - Internet-only; rate-limit
   * - IoT – Building
     - VRF-IOT
     - 300–349
     - 10.30.0.0/16
     - Per-category UNPs
   * - Voice
     - VRF-VOICE
     - 60
     - 10.60.0.0/16
     - LLDP-MED auto-VLAN
   * - Management
     - VRF-MGMT
     - 99
     - 10.99.0.0/16
     - OOB mgmt; restricted

QoS & Traffic Engineering
----------------------------

- **Classification:** DSCP/802.11e mapping at AP; CoS/DSCP trust at edge.
- **Queuing:** Priority for EF (voice), AF41/42 (video), weighted scheduling for data.
- **Rate-limits:** Guest and IoT shaping; per-SSID/per-user policers.

High Availability & Resilience
---------------------------------

- **Core:** Dual core switches with fast-converging fabric.
- **Access:** Dual-homed uplinks; optional ring topologies in outdoor/track environments.
- **WLAN:** Redundant DHCP/DNS; fast roaming; meshing only for special cases (wired preferred).

Management, Monitoring & Automation Runbooks
-----------------------------------------------

- **Provisioning:** Golden templates; Git-versioned configs; ZTP for new sites.
- **Change:** Staged rollouts; pre/post checks; automated config compliance.
- **Monitoring:** OmniVista dashboards, AIOps events, syslog/SNMP to NMS/SIEM; SLOs per SSID/role.
- **Backups:** Daily auto-backups of switch/AP configs; secure escrow of device PSKs/certs.

Security Runbook
--------------------

- Onboard users with cert-based 802.1X; fallback methods tightly scoped.
- IoT onboarding via fingerprint→UNP→container; enforce ACL minimums.
- Guest onboarding via captive portal, time-bound access, internet breakout only.
- Vulnerability/Patch cadence: monthly security updates; emergency CVE process.
- Incident response: isolate via UNP change at edge; capture PCAP on tap/SPAN; notify SOC.

