
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meridian Forward | Team 9 E-Portfolio",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Theme ----------
st.markdown("""
<style>
:root {
    --navy:#1f2738;
    --teal:#21847f;
    --mint:#e0f3ef;
    --amber:#e6a43e;
    --cream:#f8f7f3;
    --grey:#697080;
    --line:#dfe3e8;
}
.stApp { background:#f8f7f3; color:#1f2738; }
.block-container { max-width:1200px; padding-top:2rem; padding-bottom:3rem; }
h1,h2,h3 { color:#1f2738; letter-spacing:-0.02em; }
.smallcaps {font-size:.72rem;font-weight:800;letter-spacing:.12em;color:#21847f;}
.hero {
    background:linear-gradient(110deg,#e0f3ef,#eef5f7);
    border:1px solid #d6e8e5;border-radius:18px;padding:30px 34px;margin:8px 0 26px;
}
.hero h1 {font-size:2.5rem;margin:0 0 8px;}
.hero p {font-size:1.05rem;color:#4e5664;margin:0;max-width:950px;}
.insight {
    background:#1f2738;color:white;border-radius:14px;padding:22px 25px;margin:18px 0;
}
.insight h3 {color:white;margin:0 0 7px;}
.metric-card {
    background:white;border:1px solid #dfe3e8;border-radius:14px;padding:18px 18px 15px;
    min-height:118px;
}
.metric-label {font-size:.78rem;color:#697080;}
.metric-value {font-size:1.8rem;font-weight:800;color:#1f2738;margin-top:6px;}
.metric-note {font-size:.76rem;color:#697080;margin-top:4px;}
.section-card {
    background:white;border:1px solid #dfe3e8;border-radius:14px;padding:20px 22px;margin-bottom:14px;
}
.badge {
    display:inline-block;padding:5px 10px;border-radius:999px;background:#21847f;color:white;
    font-size:.72rem;font-weight:700;margin-right:6px;
}
.badge-amber {background:#e6a43e;color:#1f2738;}
.decision {
    border-left:5px solid #21847f;background:#e0f3ef;padding:16px 18px;border-radius:8px;margin:14px 0;
}
.warning {
    border-left:5px solid #e6a43e;background:#fff5df;padding:16px 18px;border-radius:8px;margin:14px 0;
}
.footer {color:#8a909b;font-size:.75rem;border-top:1px solid #dfe3e8;padding-top:14px;margin-top:35px;}
div[data-testid="stMetric"] {background:white;border:1px solid #dfe3e8;padding:12px;border-radius:12px;}
</style>
""", unsafe_allow_html=True)

# ---------- Data ----------
roles_as2 = pd.DataFrame([
    ["Engineering", 560, 640, 560, 0, 20, 20],
    ["Analytics", 368, 576, 368, 0, 11, 12],
    ["Operations", 212, 256, 212, 0, 8, 8],
    ["Data preparation", 272, 192, 192, 80, 7, 6],
    ["Quality assurance", 264, 192, 192, 72, 7, 6],
    ["Legacy experts", 192, 128, 128, 64, 9, 8],
], columns=["Role / skill","Pilot demand (h)","Usable internal supply (h)","Internal assigned (h)",
            "Gap before vendors (h)","Whole role positions","Pool people"])

pilot_roles = pd.DataFrame([
    ["Engineering", 560, 640, 560, 0, 20, 20, 0, 0],
    ["Analytics", 368, 576, 368, 0, 11, 12, 0, 0],
    ["Operations", 212, 256, 212, 0, 8, 8, 0, 0],
    ["Data preparation", 272, 192, 192, 80, 7, 6, 1, 88000],
    ["Quality assurance", 264, 192, 192, 72, 7, 6, 1, 128000],
    ["Legacy experts", 192, 128, 128, 64, 9, 8, 0, 0],
], columns=["Role / skill","Pilot demand (h)","Usable internal supply (h)","Internal assigned (h)",
            "Gap before vendors (h)","Whole role positions","Pool people","Vendor workers","Vendor cost (₹)"])

# ---------- Sidebar navigation ----------
st.sidebar.markdown("## MERIDIAN FORWARD")
st.sidebar.caption("Team 9 · HCM AS2 Case E-Portfolio")
page = st.sidebar.radio(
    "Navigate",
    [
        "01 · Case & diagnosis",
        "02 · HCM concepts",
        "03 · Workforce planner",
        "04 · Options & decision",
        "05 · Attraction, selection & onboarding",
        "06 · Evidence & assumptions",
        "07 · Revision log",
        "08 · Final recommendation",
    ],
)

# ---------- Header ----------
st.markdown("""
<div class="hero">
<div class="smallcaps">TEAM 9 · HUMAN CAPITAL MANAGEMENT · AS2</div>
<h1>Meridian Forward</h1>
<p><b>HR Alignment & Workforce Readiness — Case E-Portfolio</b><br>
A decision record showing how the business problem was diagnosed, tested through workforce planning,
and translated into a feasible HR response.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Page 1 ----------
if page == "01 · Case & diagnosis":
    st.markdown('<div class="smallcaps">01 / CASE DIAGNOSIS</div>', unsafe_allow_html=True)
    st.header("One business problem, four connected constraints")
    st.write("The case is not simply “how many people do we hire?” The workforce response must protect existing service commitments while making the proposed work executable.")

    cols = st.columns(4)
    constraints = [
        ("SKILL", "The work needs specific specialist capabilities."),
        ("TIME", "The pilot window is shorter than normal hiring lead time."),
        ("ACCESS", "Teams cannot always get the information or support they need in time."),
        ("AUTHORITY", "Important approvals remain with decision-makers elsewhere."),
    ]
    for c,(h,d) in zip(cols,constraints):
        with c:
            st.markdown(f'<div class="section-card"><div class="smallcaps">{h}</div><h3>{h.title()}</h3><p>{d}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="insight"><h3>Our diagnosis</h3><div>Meridian needs a workforce arrangement that unlocks the new work without weakening legacy service.</div></div>', unsafe_allow_html=True)

    st.subheader("What the HR response must therefore do")
    a,b,c = st.columns(3)
    with a:
        st.markdown("**1 · Make work executable**")
        st.write("Clarify work, roles, authority and coordination.")
    with b:
        st.markdown("**2 · Use deployable capacity**")
        st.write("Separate available headcount from usable hours.")
    with c:
        st.markdown("**3 · Source only the residual gap**")
        st.write("Recruit or procure after internal options are tested.")

    st.caption("Case evidence used in the team's working record includes P023–P029, P050–P052, P008–P014 and P042–P044; the exact paragraph references should be checked against the team's final case record before submission.")

# ---------- Page 2 ----------
elif page == "02 · HCM concepts":
    st.markdown('<div class="smallcaps">02 / CONCEPT APPLICATION</div>', unsafe_allow_html=True)
    st.header("HCM concepts changed the solution")
    st.write("The concepts are treated as decision tools, not as a separate theory section.")

    concept_data = [
        ["Mintzberg / decentralisation", "Decision rights", "Use bounded delegation for appropriate routine decisions while retaining reserved approvals."],
        ["Workforce planning", "Demand vs deployable supply", "Calculate usable internal capacity before deciding on external sourcing."],
        ["Job design", "Work + authority + capability", "Match specific work to role requirements rather than using a generic hiring number."],
        ["Recruitment & selection", "Targeted sourcing", "Recruit only for residual specialist gaps and test the capabilities actually required."],
        ["Onboarding / readiness", "Selected ≠ ready", "Provide access, supervision, knowledge transfer and service cover before counting new capacity."],
    ]
    df = pd.DataFrame(concept_data, columns=["Concept","Decision lens","Application to Meridian"])
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown('<div class="decision"><b>Core HCM logic:</b> Business alignment → work design → deployable capacity → decision rights → targeted sourcing → readiness.</div>', unsafe_allow_html=True)

    st.subheader("The concept-to-decision chain")
    st.code("Business priority\n      ↓\nOrganisational arrangement\n      ↓\nWork / roles / authority\n      ↓\nWorkforce demand & deployable supply\n      ↓\nInternal deployment / development / sourcing\n      ↓\nSelection + onboarding + readiness", language="text")

# ---------- Page 3 ----------
elif page == "03 · Workforce planner":
    st.markdown('<div class="smallcaps">03 / WORKFORCE PLANNER</div>', unsafe_allow_html=True)
    st.header("Test the pilot assumptions")
    st.write("This page preserves two evidence views from the team's work: the revised AS2 workforce model and the interactive pilot calculator. They should not be treated as one merged calculation.")

    st.subheader("A · Revised AS2 workforce model")
    m = st.columns(5)
    revised = [("2,320 h","Pilot demand"),("1,964 h","Usable supply"),("356 h","Net deficit"),("500 h","Gross role gaps"),("144 h","Spare capacity elsewhere")]
    for c,(v,l) in zip(m,revised):
        with c:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{l}</div><div class="metric-value">{v}</div></div>', unsafe_allow_html=True)

    st.dataframe(roles_as2, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("B · Interactive pilot calculator")
    c1,c2,c3 = st.columns(3)
    with c1:
        workflow = st.radio("Workflow arrangement", ["Retained approvals","Bounded delegation"], index=1)
    with c2:
        prep = st.radio("Customer-data preparation", ["Counted once · one owner","Included twice · baseline"], index=0)
    with c3:
        legacy = st.checkbox("Buy one legacy-expert vendor worker as fallback", value=False)

    # Calculator values from the case tool screenshots supplied by the team.
    base = {
        ("Bounded delegation","Counted once · one owner"): (1868,1652,216,2,216000),
        ("Bounded delegation","Included twice · baseline"): (2108,1652,456,6,640000),
        ("Retained approvals","Counted once · one owner"): (1960,1656,304,4,464000),
        ("Retained approvals","Included twice · baseline"): (2200,1656,544,6,640000),
    }
    demand, internal, gap, vendors, cost = base[(workflow,prep)]
    if legacy:
        vendors += 1
        cost += 120000
    budget = 600000
    remaining = budget-cost

    mm = st.columns(5)
    vals = [(f"{demand:,} h","Pilot demand"),(f"{internal:,} h","Internal hours assigned"),
            (f"{gap:,} h","Specialist gap before vendors"),(str(vendors),"Vendor workers"),(f"₹{cost:,.0f}","Vendor cost")]
    for c,(v,l) in zip(mm,vals):
        with c:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{l}</div><div class="metric-value">{v}</div><div class="metric-note">Budget remaining: ₹{remaining:,.0f}</div></div>', unsafe_allow_html=True)

    if cost <= budget and vendors <= 8:
        st.success("This scenario is within both the vendor budget and worker limit.")
    else:
        st.error("This scenario exceeds at least one model constraint.")

    st.caption("Model assumptions shown in the team's calculator include role-specific skills, no overtime, no attrition, and new hires adding 0 hours during the four-week pilot because of the stated lead time. Treat these as model assumptions, not case facts.")

# ---------- Page 4 ----------
elif page == "04 · Options & decision":
    st.markdown('<div class="smallcaps">04 / OPTION TEST</div>', unsafe_allow_html=True)
    st.header("The recommendation emerges from testing alternatives")

    comparison = pd.DataFrame([
        ["Retained approvals","Included twice",544,6,640000,"Over budget"],
        ["Retained approvals","Counted once",304,4,464000,"Within budget"],
        ["Bounded delegation","Included twice",456,6,640000,"Over budget"],
        ["Bounded delegation","Counted once",216,3,376000,"Within budget"],
    ], columns=["Workflow","Duplicate data prep","Gap before vendors (h)","Vendor workers","Vendor cost (₹)","Budget status"])
    st.dataframe(comparison.style.format({"Vendor cost (₹)":"₹{:,.0f}"}), use_container_width=True, hide_index=True)

    st.markdown('<div class="decision"><b>Decision:</b> bounded delegation + counted-once preparation is the strongest tested route because it reduces the residual gap without pushing the comparison scenario over the vendor budget.</div>', unsafe_allow_html=True)

    st.subheader("Why not simply hire?")
    reasons = [
        "The pilot is time-bound, so normal hiring lead time matters.",
        "Headcount is not the same as deployable capacity.",
        "Some apparent gaps are created by duplicated preparation or authority constraints.",
        "Legacy expertise has strategic value and should not be outsourced by default.",
    ]
    for r in reasons:
        st.markdown("• " + r)

    st.subheader("Recommended pilot response")
    st.markdown("""
**01 · Count customer-data preparation once** with one agreed output and named receiving owner.  
**02 · Use bounded delegation** for routine decisions, with clear limits and a response clock.  
**03 · Add targeted vendor support** for the specialist gaps that remain.  
**04 · Keep legacy expertise internal** and sequence the teaching requirement beyond the pilot only with service-owner agreement.  
**05 · Revisit hiring after the pilot** using measured results.
""")

# ---------- Page 5 ----------
elif page == "05 · Attraction, selection & onboarding":
    st.markdown('<div class="smallcaps">05 / EMPLOYEE LIFECYCLE RESPONSE</div>', unsafe_allow_html=True)
    st.header("Attraction → selection → onboarding")
    st.write("The employment proposition must match the authority, workload, learning opportunities and support that employees will actually receive.")

    st.subheader("Targeted roles")
    roles = [
        ("Data preparation","Residual specialist gap","Role-specific data preparation / reconciliation capability","1 targeted vendor"),
        ("Quality assurance","Residual specialist gap","Validation, exception handling and quality judgement","1 targeted vendor"),
        ("Legacy expertise","Knowledge continuity","Internal specialist knowledge; protect continuity","Retain internally"),
    ]
    df = pd.DataFrame(roles, columns=["Work area","Reason","Capability focus","Response"])
    st.dataframe(df, use_container_width=True, hide_index=True)

    a,b,c = st.columns(3)
    with a:
        st.markdown("### Attraction")
        st.write("Use targeted sourcing and internal mobility before broad external hiring.")
        st.write("Role expectations should be credible and bounded.")
    with b:
        st.markdown("### Selection")
        st.write("Use structured, role-relevant criteria and comparable assessments.")
        st.write("Avoid selection decisions based on irrelevant signals.")
    with c:
        st.markdown("### Onboarding")
        st.write("Set access, supervision, knowledge-transfer and service-cover gates.")
        st.write("A selected person becomes usable capacity only after readiness conditions are met.")

    st.markdown('<div class="warning"><b>Readiness principle:</b> “Selected” does not automatically mean “ready to deliver.”</div>', unsafe_allow_html=True)

# ---------- Page 6 ----------
elif page == "06 · Evidence & assumptions":
    st.markdown('<div class="smallcaps">06 / EVIDENCE TRAIL</div>', unsafe_allow_html=True)
    st.header("Make the reasoning auditable")

    evidence = pd.DataFrame([
        ["Case evidence","P023–P029; P050–P052","Composite problem / constraints"],
        ["Supporting case evidence","P008–P014; P042–P044","Authority, coordination and access"],
        ["Workforce model","Team 9 workbook / model","Demand, supply, role gaps and capacity"],
        ["Interactive pilot test","Meridian Workforce Planning tool screenshots","Scenario testing and budget check"],
        ["Decision record","Comparison + revision log","Why the selected response changed"],
    ], columns=["Evidence type","Reference","Use in decision"])
    st.dataframe(evidence, use_container_width=True, hide_index=True)

    st.subheader("Assumption register")
    assumptions = pd.DataFrame([
        ["Four-week pilot window","Model input used for capacity timing","Affects whether new hires add pilot hours"],
        ["Role-specific skills","Model assumption","Prevents treating all capacity as interchangeable"],
        ["No overtime","Model assumption","Makes the capacity test conservative"],
        ["No attrition during pilot","Model assumption","Keeps supply stable for the scenario"],
        ["New hires add 0 pilot hours under stated lead-time assumption","Model assumption","Prevents overstating immediate capacity"],
        ["Vendor workers are conditional","Decision rule","External sourcing follows the residual-gap test"],
    ], columns=["Assumption","Status","Effect"])
    st.dataframe(assumptions, use_container_width=True, hide_index=True)

    st.markdown("<div class='warning'><b>Important:</b> assumptions are not case facts. Before final submission, replace any placeholder assumption with the team's verified case wording or clearly retain it as an assumption.</div>", unsafe_allow_html=True)

# ---------- Page 7 ----------
elif page == "07 · Revision log":
    st.markdown('<div class="smallcaps">07 / REVISION LOG</div>', unsafe_allow_html=True)
    st.header("What changed as the model was tested?")
    st.write("This is the portfolio's learning trail: initial interpretation → test → finding → revision → final position.")

    revisions = [
        ["1","Initial view","Hiring looked like the obvious response to the apparent gap.","Treat hiring as only one option."],
        ["2","Capacity test","Available headcount did not equal deployable pilot hours.","Separate headcount from usable supply."],
        ["3","Scenario comparison","Workflow and duplicate preparation changed the apparent gap materially.","Test decision-right and workflow choices before sourcing."],
        ["4","Selected response","Bounded delegation + targeted specialist support is more feasible than broad hiring.","Use the residual gap as the sourcing trigger."],
        ["5","Legacy expertise","A 64-hour teaching gap remains outside the pilot in the recommended case.","Protect internal legacy knowledge and sequence the teaching block."],
    ]
    df = pd.DataFrame(revisions, columns=["Step","Stage","What we learned","Revision"])
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown('<div class="insight"><h3>Learning captured</h3><div>The best HR response is the one that makes the work deployable — not the one that simply increases headcount.</div></div>', unsafe_allow_html=True)

    st.subheader("Carry-forward into AS3 / AS4")
    st.markdown("""
- Re-test whether the pilot changes the longer-term workforce requirement.
- Carry unresolved authority and coordination issues into performance and employee-relations design.
- Use measured pilot outcomes to revisit recruitment and development decisions.
- Preserve a dated record of challenges, revisions and what was learned.
""")

# ---------- Page 8 ----------
elif page == "08 · Final recommendation":
    st.markdown('<div class="smallcaps">08 / FINAL CASE POSITION</div>', unsafe_allow_html=True)
    st.header("Unblock the work before adding more people.")

    st.markdown('<div class="insight"><h3>Recommended HR response</h3><div>Align decision rights, work design, deployable capacity and targeted sourcing so Meridian can deliver the pilot while protecting existing service commitments.</div></div>', unsafe_allow_html=True)

    cols = st.columns(4)
    final = [
        ("DECISION RIGHTS","Use bounded delegation for routine decisions."),
        ("WORKFORCE","Use internal deployable capacity first."),
        ("SOURCING","Target residual specialist gaps."),
        ("KNOWLEDGE","Keep legacy expertise internal."),
    ]
    for c,(h,d) in zip(cols,final):
        with c:
            st.markdown(f'<div class="section-card"><div class="smallcaps">{h}</div><h3>{h.title()}</h3><p>{d}</p></div>', unsafe_allow_html=True)

    st.subheader("Decision metrics")
    a,b,c,d,e = st.columns(5)
    for col,val,label in zip(
        [a,b,c,d,e],
        ["2,320 h","1,964 h","356 h","500 h","144 h"],
        ["revised pilot demand","usable supply","net deficit","gross role gaps","spare elsewhere"]
    ):
        with col:
            st.metric(label,val)

    st.markdown('<div class="warning"><b>Do not overclaim:</b> the interactive pilot calculator and the revised AS2 model are distinct model views. Explain their inputs and purpose in the defence rather than presenting them as one calculation.</div>', unsafe_allow_html=True)

    st.subheader("The final test")
    st.write("Can every major recommendation be defended by linking a business need → HCM concept → case evidence → calculation/assumption → decision?")
    st.success("If yes, the portfolio is doing its job.")

st.markdown('<div class="footer">Meridian Forward · Team 9 · HCM AS2 · Case-solving e-portfolio · Built as a supporting decision record for presentation and defence.</div>', unsafe_allow_html=True)
