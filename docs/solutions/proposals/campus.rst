====================================================
Campus/Enterprise Network Architecture
====================================================

:Document Title:  Technical Proposal – Network Infrastructure Modernization
:Submitted By:    Alcatel-Lucent Enterprise
:Revision:        1.0


1. Executive Summary
====================

The Proposed Solution shall deliver a secure, resilient, and scalable enterprise network infrastructure
supporting wired, wireless, and hybrid-cloud connectivity.  It shall provide end-to-end high availability,
zero-trust security, and centralized visibility to meet the Authority’s/Customer **(delete appropriate)** operational and compliance objectives.

Key features include:

* Three-tier redundant **Campus LAN/WLAN**
* **EVPN Data Center** spine-leaf fabric
* **Hybrid Cloud** integration (AWS/Azure)
* **SD-WAN/Internet Edge** with dual ISPs
* **Unified Communication** and **Remote Access VPN**
* Centralized Management, identity, telemetry, and automation services


2. Scope and Objectives
=======================

The scope of this project shall encompass design, supply, installation, configuration, testing,
and commissioning of the enterprise network infrastructure, including:

* Campus switching and wireless systems
* Data-center fabric, Data Center interconnect, and Data-to-cloud connectivity
* Internet & VPN connectivity
* Unified communications integration
* Network security, access control, and monitoring
* Ongoing support, training, and documentation

**Objectives**

* Modernize the existing network to support digital-first services
* Transform the Wireless network to Wi-Fi 6/6E/7 **(delete appropriate)** technology to improve coverage and experiences.
* Enhance availability to ≥ 99.95 % uptime
* Improve performance and scalability through automation and SD-WAN
* Strengthen cybersecurity posture through segmentation, least privilege access, identity management, and MFA


3. Existing Environment
=======================

The current environment consists of legacy L2/L3 switching and independent WLAN controllers.
It lacks unified management, network policy control, dynamic routing, and centralized visibility.
Poor wireless coverage and performance to support high bandwidth applications.
Performance degradation and manual configuration have resulted in limited scalability.
The proposed modernization shall address these constraints through an integrated, modular architecture.


4. Proposed Solution Overview
=============================

The Proposed Solution shall introduce a unified, service-oriented architecture
covering access (wired and wireless), aggregation **(delete appropriate)**, core, data-center, and cloud domains.

Key Design Principles
----------------------

* High availability and fault tolerance – no single point of failure
* Modular scalability – independent growth of domains
* Standards-based interoperability (IEEE, IETF)
* Zero-Trust security and Identity management with Microsoft Entra ID **(delete appropriate)**
* End-to-end QoS policy control for different class of applications (Gold/Silver/Bronze)
* Centralized monitoring, automation, and analytics


5. Solution Architecture Principles
===================================

* **Resiliency:**  Dual control modules & fabric, redundant PSUs, Virtual Chassis, RSTP, LACP, BFD-assisted OSPF/BGP routing, and ECMP.
* **Redundancy:**  Hardware, link, and power-feed duplication across all layers.
* **Security:**  VRF/VLAN for macro segmentation, Role-based with ACL for micro-segmentation, 802.1X/MAB, and identity & MFA management.
* **Scalability:**  Horizontal expansion through stackable or leaf-spine designs.
* **Operational Efficiency:**  Single-pane-of-glass management with OmniVista 2500/Cirrus **(delete appropriate)**, Infrastructure-as-Code (IaC) deployment, API-based integration,
  and automated configuration validation.


6. Proposed Architecture and Design
===================================

6.1 High-Level Architecture Overview
------------------------------------

High-level architecture diagram

.. image:: https://ale-nbd-docs.readthedocs.io/en/latest/_static/images/hld-campus-architecture.png
   :alt: Campus Network Architecture
   :align: center
   :width: 70%

\

The Proposed Solution shall comprise six (6) inter-connected network domains:

#. Campus LAN, and WLAN with Distributed WLAN Architecture
#. EVPN Data Center (Spine-Leaf Fabric)
#. Hybrid Cloud (AWS/Azure Connectivity)
#. Internet Edge and SD-WAN Perimeter
#. Unified Communication (Voice/Video/Collaboration)
#. Remote VPN / Work-from-Home Access

All components shall be engineered with redundancy at device, link, and control-plane levels,
ensuring *no single point of failure*.


6.2 Detailed Architecture by Domain
-----------------------------------

6.2.1 Campus LAN / WLAN (Three-Tier Architecture)/(Two-Tier Architecture) **(delete appropriate)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Overview**

The Campus network shall adopt a **Three-Tier Architecture**/ **Two-Tier Architecture** **(delete appropriate)** consisting of **Core**, **Distribution** **(delete appropriate)**,
and **Access** layers, each engineered for redundancy, resiliency, and deterministic convergence.

**A. Core Layer** **(please adapt for Virtual Chassis)**

* Two (2) or more high-performance core switches in redundant pair.
* Dual supervisors, fabric modules, PSUs, and hot-swappable interface cards.
* Inter-core 40/100 Gbps LACP links; ECMP routing toward Distribution.
* **OSPF + BFD** for sub-second failover; **NSF/GR** for control-plane stability.
* Dual uplinks from every Distribution pair to both Core nodes.

**B. Distribution Layer** **(please adapt for Virtual Chassis)** **(delete appropriate)**

* Redundant Distribution pairs with **Virtual Chassis** or equivalent to Access.
* Dual supervisors and PSUs per chassis.
* **MVRP** for dynamic VLAN registration.
* **RSTP/MSTP** for L2 recovery < 2s recovery.
* **HSRP/VRRP** default-gateway redundancy.
* **OSPF + BFD** uplinks to Core; inter-distribution link for sync.

**C. Access Layer**

* Stack/Virtual-Chassis access switches with ISSU support.
* **MVRP** for dynamic VLAN registration
* Dual LACP uplinks to both Distribution switches.
* 802.1X/MAB NAC enforcement; DHCP Snooping / ARP Inspection.
* Dual power feeds and PoE priority for critical devices.

**D. Wireless LAN Subsystem**

* OmniVista 2500/Cirrus centralized WLAN management. **(delete appropriate)**
* Wi-Fi 6/6E/7 **(delete appropriate)** APs with 802.11r/k/v fast roaming.
* APs powered via PoE+ switches.
* Auto RF optimization and automatic channel/power adjustment.
* L2 and L3 roaming support.
* WPA2/WPA3 personal and Enterprise security modes.
* 802.1X/MAC and RADIUS integration.
* Microsoft Entra ID **(delete appropriate)** for identity-based access control.
* Bonjour/mDNS service discovery.
* wIDS/IPS with dedicated scanning radio **(delete appropriate)**
* Rogue AP detection and containment.
* Role-based WLAN segmentation (Corp, Guest, IoT, Voice).
* L2-L7 access-control
* QoS for voice/video prioritization.
* IoT analytics and device profiling.
* Guest Management and Captive Portal support.
* Guest onboarding via self-service portal, vouchers, sponsor approval, social media login (Facebook/Google).
* BYOD onboarding
* Heatmap & Floorplan visualization.
* Client/AP analytics and reporting.


**E. Operational Resilience**

.. list-table:: 
   :header-rows: 1
   :widths: 20 40 40

   * - **Layer**
     - **Redundancy Measures**
     - **Convergence / Protection**
   * - Core
     - Dual nodes, LACP links, dual PSUs
     - OSPF + BFD + ECMP + GR/NSF
   * - Distribution
     - MLAG, dual PSUs, HSRP/VRRP
     - RSTP / MSTP
   * - Access
     - Stack/VC, dual uplinks (LACP)
     - ISSU + Edge Security + PoE Redundancy
   * - WLAN
     - Overlapped Radio coverage, Redundant management
     - 802.11r/k/v Fast Failover, wIDS/IPS Rogue AP Containment


6.2.2 EVPN Data Center (Spine/Leaf Fabric)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Data Center Fabric shall adopt a **spine-and-leaf** architecture consisting of **10/25/40/50/100 Gbe** **(delete appropriate)** spine and leaf nodes.
The Data Center shall support east-west traffic patterns, workload mobility, and multi-tenancy through VXLAN/EVPN overlays.

* Non-blocking **Spine-Leaf** topology with Layer 3 links for **ECMP** load-balancing.
* Each Leaf dual-homed to Spines; underlay OSPF for IGP with BFD for fast convergence.
* VXLAN overlay with **EVPN Multihoming (EVPN-MH)** for active-active links.
* Distributed anycast gateways for workload mobility, and optimal routing.

A pair of DC-edge leaf nodes to provide connectivity to campus core and the Internet.

6.2.3 Hybrid Cloud (AWS/Azure Integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The network shall connect to AWS Private cloud via  **Direct Connect / Transit Gateway** over the Internet via separate PoPs/providers.
* Segregated VRFs/VPCs for Prod/Dev/DR environments.
* BGP to OSPF redistribution for routes convergence.


6.2.4 Internet Edge and SD-WAN Perimeter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Dual firewalls (Active/Active or Standby) with state synchronization.
* Dual edge routers with dual ISPs using eBGP multi-homing.
* **SD-WAN fabric** over Internet/MPLS/5G **(delete appropriate)** underlays.
* Application-aware path selection.
* Dual SD-WAN controllers in HA mode / CLoud controller **(delete appropriate)**.


6.2.5 Unified Communication (Voice / Video / Collaboration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Redundant Call Manager servers.
* vSBC gateway with HA for SIP trunks to telco/carriers.
* Branch Survivable Remote Gateways for WAN failover.
* QoS: EF (RTP), AF41 (Video), CS3 (Signaling).
* SRTP and TLS for media and signaling encryption.
* IP Phones (wired/Wi-Fi/Dect) auto-provisioning via TFTP/HTTP(S).
* Unified Communications service such as presence, voicemail, conferencing, and collaboration tools integration.
* Softphone and mobile client support.


6.2.6 Remote VPN / Work-from-Home
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Dual VPN concentrators/Firewall in HA cluster with session replication.
* IPsec/SSL VPN with Dead Peer Detection (DPD).
* Zero-Trust policies with MFA, posture assessment, dynamic ACLs.
* Split/full tunnel modes as approved by the Authority.


6.3 Network Services (Common Across Domains)
--------------------------------------------

* **Routing:** OSPF / BGP with GR, NSF, and BFD (200–500 ms).
* **IP Services:** Redundant DNS/DHCP servers with synchronized IPAM.
* **AAA/NAC:** Centralized RADIUS / TACACS+ with redundant nodes.
* **Management:** Web GUI/SSH/SNMP using secure protocols (SSH v2, HTTPS, SNMP v3).


6.4 Addressing, Segmentation and Traffic Engineering
----------------------------------------------------

This section defines the hierarchical IP addressing plan for the entire network topology, including
data centers, campus core, wireless, WAN, and cloud connectivity. All addressing uses RFC1918 private
address space for internal routing.


Summary by Function
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Function / Zone
     - Range
     - Purpose
   * - Core & DC Backbone
     - 10.0.0.0/16
     - Core interconnects between firewalls, cores, DC spines, and WAN
   * - Data Center 1
     - 10.1.0.0/16
     - DC1 spines, leafs, edge switches, and servers
   * - Data Center 2
     - 10.2.0.0/16
     - DC2 spines, leafs, edge switches, and servers
   * - Campus Distribution & Access
     - 10.3.0.0/16
     - Distribution and access switches, client VLANs
   * - Wireless Network
     - 10.4.0.0/15
     - AP management and client VLANs
   * - WAN & Internet Edge
     - 10.6.0.0/16
     - WAN switches, Internet, and cloud uplinks
   * - AWS Cloud
     - 10.7.0.0/16
     - AWS VPC servers and VPN/Direct Connect links
   * - Management Network
     - 10.8.0.0/16
     - Out-of-band management and monitoring services


Core & Firewall Interconnects
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 35 15 50

   * - Segment
     - CIDR
     - Description
   * - Core1 ↔ Core2
     - 10.0.0.0/30
     - Core redundancy link
   * - Core1 ↔ FW1
     - 10.0.0.4/30
     - Internal interface to FW1
   * - Core2 ↔ FW2
     - 10.0.0.8/30
     - Internal interface to FW2
   * - FW1 ↔ FW2 HA
     - 10.0.0.12/30
     - Firewall sync/HA link
   * - Core ↔ WAN
     - 10.0.0.16/29
     - Link between core and WAN switches


Data Center Networks
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Zone
     - CIDR
     - Usage
   * - DC1 Spine-Leaf Fabric
     - 10.1.0.0/20
     - Interconnect between spines and leafs
   * - DC1 Servers
     - 10.1.16.0/21
     - ~200 servers
   * - DC2 Spine-Leaf Fabric
     - 10.2.0.0/20
     - Interconnect between spines and leafs
   * - DC2 Servers
     - 10.2.16.0/21
     - ~200 servers
   * - Fabric Services
     - 10.1.32.0/22, 10.2.32.0/22
     - vMotion, storage, and infra VLANs


Campus Distribution & Access
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Zone
     - CIDR
     - Purpose
   * - Distribution Switches
     - 10.3.0.0/23
     - Loopbacks and uplinks
   * - Edge Switches
     - 10.3.2.0/20
     - 400 edge switches, each with /30 or /31 uplinks
   * - Access VLANs
     - 10.3.16.0/20
     - Client VLANs for wired access


Wireless Network
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Zone
     - CIDR
     - Usage
   * - AP Management
     - 10.4.0.0/22
     - 2000 access points
   * - Client VLAN Pool
     - 10.4.4.0/15
     - 10,000 clients (segmented by role)


Client VLAN Role Breakdown
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 10 25 15 40

   * - VLAN ID
     - Role / Department
     - Subnet
     - Description / Notes
   * - 100
     - Corporate Staff – HQ
     - 10.4.4.0/24
     - Standard users in HQ building
   * - 101
     - Corporate Staff – Block A
     - 10.4.5.0/24
     - Admin & HR offices
   * - 102
     - Corporate Staff – Block B
     - 10.4.6.0/24
     - Finance, procurement
   * - 103
     - Corporate Staff – Block C
     - 10.4.7.0/24
     - Marketing, sales teams
   * - 104
     - Corporate Staff – R&D
     - 10.4.8.0/24
     - Development & engineering users
   * - 105
     - Guest Wi-Fi – HQ
     - 10.4.9.0/24
     - Internet-only guest VLAN
   * - 108


Client VLAN Role Breakdown
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 10 25 15 40

   * - VLAN ID
     - Role / Department
     - Subnet
     - Description / Notes
   * - 100
     - Corporate Staff – HQ
     - 10.4.4.0/24
     - Standard users in HQ building
   * - 101
     - Corporate Staff – Block A
     - 10.4.5.0/24
     - Admin & HR offices
   * - 102
     - Corporate Staff – Block B
     - 10.4.6.0/24
     - Finance, procurement
   * - 103
     - Corporate Staff – Block C
     - 10.4.7.0/24
     - Marketing, sales teams
   * - 104
     - Corporate Staff – R&D
     - 10.4.8.0/24
     - Development & engineering users
   * - 105
     - Guest Wi-Fi – HQ
     - 10.4.9.0/24
     - Internet-only guest VLAN
   * - 108
     - IoT / Smart Devices
     - 10.4.12.0/24
     - IP cameras, printers, sensors
   * - 114
     - Finance Restricted
     - 10.4.18.0/24
     - Financial systems VLAN
   * - 117
     - IT Admin VLAN
     - 10.4.21.0/24
     - Network admin systems
   * - 128
     - Surveillance VLAN
     - 10.4.32.0/24
     - CCTV and security devices
   * - 129
     - Voice VLAN
     - 10.4.33.0/24
     - IP telephony
   * - 131
     - Staff BYOD VLAN
     - 10.4.35.0/24
     - Employee personal devices
   * - 139
     - Temporary VLAN 2
     - 10.4.43.0/24
     - Overflow or temporary use


WAN & Cloud
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Zone
     - CIDR
     - Usage
   * - WAN Switches
     - 10.6.0.0/28
     - WAN switch interconnect and mgmt
   * - Internet Edge
     - 10.6.0.16/28
     - ISP handoff and DMZ
   * - AWS VPN / Direct Connect
     - 10.7.0.0/24
     - Tunnel endpoints
   * - AWS Servers
     - 10.7.1.0/24
     - 100 servers hosted in AWS


Management Network
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Zone
     - CIDR
     - Usage
   * - OOB Management
     - 10.8.0.0/20
     - Switches, firewalls, LAN/WLAN Management
   * - NMS & Monitoring
     - 10.8.16.0/22
     - Syslog, Radius, SNMP, and monitoring

------------------------
Addressing Summary
------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 20 40

   * - Category
     - Count
     - Subnet Size
     - Coverage
   * - Access Points
     - 2000
     - /22
     - 4096 IPs
   * - Edge Switches
     - 400
     - /20
     - 4096 IPs
   * - Clients
     - 10,000
     - /15
     - 131,072 IPs
   * - On-Prem Servers
     - 500
     - /21 per DC
     - 4096 IPs total
   * - AWS Servers
     - 100
     - /24
     - 256 IPs
   * - Management
     - ~1000
     - /20
     - 4096 IPs   



6.5 Security and Compliance
---------------------------

The network **shall implement** a multi-layered security framework to protect against internal and external threats, ensuring data confidentiality, integrity, and availability.
The security architecture **shall include**, but not limited to, the following components:

* Zero Trust Network Architecture (ZTNA) principles.
* Network Access Control (NAC) with 802.1X/MAB and RADIUS integration.
* Role-Based Access Control (RBAC) for device and network access.
* Strong authentication with MFA for administrative and user access.
* Network segmentation and micro-segmentation. 
* Encrypted management and data-plane traffic (SSH, HTTPS, IPsec, TLS). 
* Defense-in-depth architecture with segmentation, NAC, firewalls, IDS/IPS, SIEM.
* Log retention ≥ 12 months; forward to central SIEM.
* Common criteria certification
* FIPS 140-2 compliance


6.6 Monitoring, Telemetry and Automation
----------------------------------------

* Real-time telemetry (SNMP v3, sFlow, RMON).
* Site availability ≥ 99.95 %; routing convergence ≤ 500 ms (BFD).
* Monthly SLA and capacity reports (ports, APs, Switches).


7. Bill of Materials (BOM) and Licensing
=========================================

The Bidder **shall supply** all required active and passive components,
including switches, routers, controllers, APs, firewalls, servers, optics, cables,
and associated software licenses.

<Placeholder for BOM table>

.. list-table::
   :header-rows: 1
   :widths: 25 35 10 15 15

   * - Item
     - Description
     - Quantity
     - Unit Price
     - Total Price
   * - Campus Core Switches
     - High-performance core switches
     - 2
     - $XX,XXX
     - $XX,XXX
   * - Campus Distribution Switches
     - Redundant distribution switches
     - 4
     - $XX,XXX
     - $XX,XXX
   * - Campus Access Switches
     - Stackable access switches
     - XX
     - $X,XXX
     - $XX,XXX
   * - Wireless Access Points
     - Wi-Fi 6/6E/7 APs
     - XX
     - $X,XXX
     - $XX,XXX
   * - Data Center Spine Switches
     - High-capacity spine switches
     - 4
     - $XX,XXX
     - $XX,XXX
   * - Data Center Leaf Switches
     - Leaf switches
     - 8
     - $XX,XXX
     - $XX,XXX
   * - Firewalls
     - Dual firewalls for Internet Edge
     - 2
     - $XX,XXX
     - $XX,XXX
   * - Software Licenses
     - Network OS and feature licenses
     - XX
     - $X,XXX
     - $XX,XXX






----

**End of Document**
