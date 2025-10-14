Data Center Interconnect (DCI)
==============================

A resilient Data Center Interconnect (DCI) enables seamless workload mobility, active-active data center operations, disaster recovery, and business continuity. Alcatel-Lucent Enterprise (ALE) supports multiple DCI architectures to interconnect geographically distributed data centers while ensuring Layer 2/Layer 3 extension, segmentation, and policy consistency.

This section outlines three validated DCI options based on architectural preference and interoperability requirements:

- **VXLAN Gateway (Overlay-based DCI)**
- **SPB over GRE Tunnel**
- **EVPN-VXLAN (Standards-based Fabric Interconnect)**

.. contents::
   :depth: 2
   :local:


DCI Using VXLAN Gateway (Overlay)
----------------------------------

**Overview**

This approach uses ALE OmniSwitch platforms as VXLAN Layer 2/Layer 3 Gateways to encapsulate intra-DC VLANs into VXLAN tunnels for inter-DC transport. It is ideal for extending VLANs across sites without requiring underlying WAN changes.

**Key Characteristics**

- Overlay encapsulation using VXLAN (VNI-based)
- Active-active support for VM mobility and workload balancing
- Independent of WAN underlay (works over any IP/MPLS network)

**Use Cases**

- Workload mobility (e.g., VMware vMotion, clustering)
- Layer 2 extension between DCs
- Rapid deployment where WAN cannot be modified

**Advantages**

- Fast, easy deployment
- Simple operation with native OmniSwitch integration
- Scalable segmentation using VNIs

**Considerations**

- Flood-and-learn control plane (no EVPN)
- Less scalable for large multi-tenant environments without orchestration


DCI Using SPB over GRE Tunnel
-----------------------------

**Overview**

This method extends SPB (Shortest Path Bridging) fabric across data centers using GRE tunnels. It preserves ALE’s Intelligent Fabric (iFab) service automation and enables deterministic Layer 2/Layer 3 extension across IP WANs.

**Key Characteristics**

- SPB Virtual Service Networks (VSNs) encapsulated in GRE
- End-to-end fabric path control with fast convergence
- Extended Layer 2/Layer 3 virtualization without redesign

**Use Cases**

- Multi-site fabric extension
- Data centers already using SPB campus fabrics
- Fabric automation with iFab and auto-attach

**Advantages**

- Consistent SPB service model across DCs
- Seamless L2/L3 VSN continuity
- Zero manual VLAN stitching

**Considerations**

- WAN must support GRE/IP encapsulation
- Best suited for ALE fabric environments (less multi-vendor)


DCI Using EVPN-VXLAN
---------------------

**Overview**

EVPN-VXLAN provides a fully standards-based DCI using BGP EVPN for control-plane signaling. It enables MAC/IP learning across DC sites with scalable routing, segmentation, and tenant isolation.

**Key Characteristics**

- Standards-based BGP EVPN control plane
- Integrated Layer 2 and Layer 3 interconnect with IRB
- High scalability for multi-tenant cloud/DC environments

**Use Cases**

- Hybrid cloud and multi-vendor DC integration
- Large-scale multi-tenant data centers
- Disaster recovery with active-active architectures

**Advantages**

- Efficient MAC/IP control plane (no flooding)
- Full interoperability with service provider EVPN backbones
- Strong tenant and VRF isolation

**Considerations**

- Requires BGP and routing expertise
- Higher operational complexity


DCI Solution Selection Guidance
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20

   * - **Criteria**
     - **VXLAN Gateway**
     - **SPB over GRE**
     - **EVPN-VXLAN**
   * - **Control Plane**
     - Flood & Learn
     - SPB IS-IS Fabric
     - BGP EVPN
   * - **Multi-Tenancy Scale**
     - Medium
     - Medium
     - High
   * - **Interoperability**
     - Multi-Vendor
     - Multi-Vendor
     - Multi-Vendor
   * - **Operational Simplicity**
     - High
     - High
     - Moderate
   * - **Ideal Use Case**
     - Fast L2 Extension
     - Fabric Extension
     - Cloud / Multi-DC Integration


