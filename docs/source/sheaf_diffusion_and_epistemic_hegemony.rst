Sheaf Diffusion and Epistemic Hegemony
=======================================
This document describes the implementation of the sheaf diffusion process and the Epistemic Hegemony model in the codebase.

Sheaf Diffusion
----------------
The sheaf diffusion process is implemented as a continuous-in-time message passing Graph Neural Network (GNN). The process is defined by the following equation: 
- Initial condition: :math:`\\mathbf{X}(0)=\\mathbf{X}`
- Evolution rule: :math:`\\dot{\\mathbf{X}}(t)=-\\Delta_{\\mathcal{F}} \\mathbf{X}(t)`

Epistemic Hegemony
-------------------
The Epistemic Hegemony model is implemented using the sheaf diffusion process. The model includes methods for setting the initial state of the system and updating the state according to the dynamics of Epistemic Hegemony. The model also includes a method for calculating the epistemic arbitrage equilibrium.