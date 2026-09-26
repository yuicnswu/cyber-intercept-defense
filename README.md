# Edge-Cloud Scam Defense Architecture**

**Project:** Edge-Cloud Semantic Intent Observer
**Format:** Deep Technical & Market Review
**Overall Assessment:** 9.0 / 10

---

## 📝 PAPER EXTRACT: Rationale, Architecture, & Evaluation Methodology
*(Note: You can copy and paste the following sections directly into your academic paper).*

### 1. Rationale: The Fundamental Gap in Existing Paradigms
The fundamental limitation of contemporary financial fraud defense mechanisms is their reliance on **post-transaction anomaly detection** and **static metadata blacklisting**. These legacy paradigms fail catastrophically against Zero-Day Social Engineering and Authorized Push Payment (APP) fraud. In these attacks, the adversary psychologically manipulates the user into bypassing cryptographic multi-factor authentication (MFA) themselves. The system successfully verifies the *identity* of the user, but remains entirely blind to the coerced *intent* of the transaction.

Furthermore, current defense mechanisms suffer from structural **Information Asymmetry (Silo Blindness)**. Telecommunication providers have visibility into the coercive communications (SMS/Calls) but lack financial context, whereas financial institutions observe the transaction but lack visibility into the psychological coercion preceding it ($\mathcal{I}_{\text{bank}} \cap \mathcal{I}_{\text{carrier}} = \emptyset$). Attempting to solve this by streaming all user communications to a centralized cloud AI introduces unacceptable latency and violates stringent privacy regulations (e.g., PDPA, GDPR).

### 2. The Proposed Architecture: 3-Tier Edge-Cloud Semantic Observer
To bridge this gap, we propose a novel **Pre-transaction Edge-Cloud Semantic Intent Architecture**. The workload is partitioned using a Pareto-optimized distribution to satisfy strict latency and privacy bounds.

*   **Tier 1: Edge TEE (Trusted Execution Environment)**
    Operating directly on the user's mobile device, this layer intercepts incoming communications via authorized OS APIs (e.g., Android Notification Listener). A highly quantized Small Language Model (SLM), running entirely within a hardware-isolated Secure Enclave (e.g., ARM TrustZone), evaluates the text for psychological heuristics (Authority Claim, Urgency Framing). It computes a localized Semantic Intent Vector ($s_{\text{risk}} \in \mathbb{R}^d$) without ever exfiltrating plaintext user messages, guaranteeing zero data leakage.
*   **Tier 2: Cloud Graph Intelligence**
    If the Edge vector $s_{\text{risk}}$ exceeds a preliminary uncertainty threshold, the device transmits a differentially private cryptographic signature (e.g., SimHash) to the Cloud. This layer utilizes Graph Neural Networks (GNNs) to correlate the signature against a global threat topology $\mathcal{G} = (\mathcal{V}_{\text{entity}}, \mathcal{E}_{\text{flow}})$, checking for newly registered domains, burner phone clusters, and mule account networks.
*   **Tier 3: Bayesian Policy & UI Intervention**
    The final decision engine merges the Edge semantic score and the Cloud graph score. The intervention is governed by **Bayesian Cost-Asymmetric Decision Theory**. Because the cost of a false negative (financial ruin) drastically outweighs a false positive (UX friction), the system mathematically bounds the intervention threshold ($C_{FN} \gg C_{FP}$). It triggers a UI interruption (e.g., a "Cooling-Off" modal or Step-Up Authentication) precisely at the Trust Boundary—right before the user hits the transfer button.

### 3. Evaluation Methodology: How to Measure System Efficacy
To rigorously validate the proposed architecture, we define five orthogonal evaluation metrics across Security, Systems, and Human-Computer Interaction (HCI):

*   **Metric 1: Constrained Recall (Efficacy)**
    In high-friction financial environments, minimizing false alarms is critical to prevent warning fatigue. We measure the system's True Positive Rate (Recall) strictly bounded by a maximum acceptable False Positive Rate ($FPR \le 0.1\%$). Success is defined as achieving a statistically significant recall improvement (e.g., $\ge 10$ percentage points) over baseline heuristic rules at this fixed FPR.
*   **Metric 2: Adversarial Robustness (Evasion)**
    To measure resilience against adaptive attackers, we evaluate the model's degradation against an adversarial "Evasion Dataset." This dataset introduces structural perturbations (e.g., homoglyph substitutions, zero-width characters, spacing obfuscation) bounded by a $k$-edit distance $\mathcal{A} = \{ x' \mid d_{\text{edit}}(x, x') \le k \}$.
*   **Metric 3: Pre-Transaction Timeliness (Lead Time)**
    Unlike traditional systems that measure time-to-detection post-fraud, we introduce *Lead Time*. This is measured as the median temporal delta (in seconds or number of dialogue turns) between the system's first internal risk flag and the adversary's actual request for a money transfer. A successful system must yield a positive Lead Time ($\Delta t > 0$).
*   **Metric 4: System Overhead (Latency & Edge Footprint)**
    We measure the p95 inference latency on mid-tier mobile hardware (e.g., Snapdragon 7-series), with a target upper bound of $\le 300\text{ms}$ to ensure seamless UX. We also quantify the peak memory footprint (RAM allocation) of the quantized SLM to prove viability on consumer devices.
*   **Metric 5: HCI Compliance Rate**
    Through a simulated, IRB-approved user study, we measure the proportion of users who abandon a simulated coercive transfer when presented with the Bayesian warning UI, compared to a control group utilizing standard OS-level warnings. Success is measured via a Chi-square test of independence ($p < 0.05$).

---

## 1. Core Innovation & Market Disruption 
**The Market Problem:** Authorized Push Payment (APP) fraud is a multi-billion dollar crisis. Legacy systems operate on *post-transaction* anomaly detection. 
**The Disruptive Innovation:** This architecture shifts the paradigm from post-transaction reaction to **pre-transaction semantic intervention**. By running SLMs locally, the system detects psychological coercion *before* the user hits transfer, creating a massive moat for FinTech liability reduction.

## 2. Academic References & Citation Impact
1. **[Edge-Cloud Architecture]** Mao, Y., You, C., Zhang, J., Huang, K., & Letaief, K. B. (2017). *A survey on mobile edge computing.* IEEE Communications Surveys & Tutorials. **(Cited by ~10,500+)**
2. **[Information Asymmetry]** Anderson, R. (2001). *Why information security is hard-an economic perspective.* ACSAC. **(Cited by ~2,600+)**
3. **[Adversarial Robustness]** Madry, A., et al. (2018). *Towards Deep Learning Models Resistant to Adversarial Attacks.* ICLR. **(Cited by ~14,200+)**
4. **[Cost-Asymmetric Decisions]** Elkan, C. (2001). *The foundations of cost-sensitive learning.* IJCAI. **(Cited by ~3,800+)**
5. **[HCI & Warning Fatigue]** Akhawe, D., & Felt, A. P. (2013). *Alice in Warningland.* USENIX. **(Cited by ~1,300+)**
