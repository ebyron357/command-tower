#!/usr/bin/env python3
"""Generate Command Tower Claude Company OS skills, agents, commands, and registries.

This script materializes approved capabilities from an in-repo inventory.
It is idempotent for content it owns and never writes secrets.
"""
from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = date.today().isoformat()


@dataclass
class Cap:
    id: str
    name: str
    department: str
    type: str  # skill|subagent|command|plugin|mcp|hook|governing|validation|external|reference
    purpose: str
    business_value: str
    trigger: str
    positive: list[str]
    negative: list[str]
    source: str = "internal-reconstruction"
    source_commit_or_version: str = "company-os-v1"
    license: str = "Apache-2.0"
    trust_level: str = "internal"
    installation_method: str = "project-files"
    dependencies: list[str] = field(default_factory=list)
    required_tools: list[str] = field(default_factory=lambda: ["Read", "Write", "Grep", "Glob"])
    required_credentials: list[str] = field(default_factory=list)
    permissions: list[str] = field(default_factory=lambda: ["read-repo", "write-project-docs"])
    risk_level: str = "low"
    status: str = "implemented"
    validation: str = "structure-validated"
    overlaps: list[str] = field(default_factory=list)
    supersedes: list[str] = field(default_factory=list)
    superseded_by: str = ""
    owner: str = "command-tower"
    notes: str = ""
    origin: str = "newly-designed"  # recovered|newly-designed
    workflow_steps: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    safety: list[str] = field(default_factory=list)
    allowed_tools: list[str] = field(default_factory=list)
    prohibited: list[str] = field(default_factory=list)


def inventory() -> list[Cap]:
    caps: list[Cap] = []

    def skill(dept, slug, purpose, value, trigger, pos, neg, **kw):
        caps.append(Cap(
            id=f"skill.{slug}",
            name=slug,
            department=dept,
            type="skill",
            purpose=purpose,
            business_value=value,
            trigger=trigger,
            positive=pos,
            negative=neg,
            workflow_steps=kw.get("steps", [
                "Clarify objective, constraints, and success criteria",
                "Gather required repository and stakeholder context",
                "Execute the department workflow with evidence",
                "Produce structured outputs and verification notes",
                "Escalate risks and document residual uncertainty",
            ]),
            outputs=kw.get("outputs", ["Structured deliverable", "Assumptions list", "Verification notes"]),
            safety=kw.get("safety", [
                "Do not invent evidence",
                "Do not expose secrets",
                "Do not claim credentials work without testing",
            ]),
            overlaps=kw.get("overlaps", []),
            notes=kw.get("notes", ""),
            origin=kw.get("origin", "newly-designed"),
            required_tools=kw.get("required_tools", ["Read", "Write", "Grep", "Glob", "Shell"]),
        ))

    def agent(dept, slug, purpose, value, trigger, pos, neg, tools, prohibited, **kw):
        caps.append(Cap(
            id=f"agent.{slug}",
            name=slug,
            department=dept,
            type="subagent",
            purpose=purpose,
            business_value=value,
            trigger=trigger,
            positive=pos,
            negative=neg,
            allowed_tools=tools,
            prohibited=prohibited,
            required_tools=tools,
            overlaps=kw.get("overlaps", []),
            notes=kw.get("notes", ""),
            origin=kw.get("origin", "newly-designed"),
            risk_level=kw.get("risk_level", "medium"),
        ))

    def command(dept, slug, purpose, value, trigger, pos, neg, **kw):
        caps.append(Cap(
            id=f"cmd.{slug}",
            name=slug,
            department=dept,
            type="command",
            purpose=purpose,
            business_value=value,
            trigger=trigger,
            positive=pos,
            negative=neg,
            overlaps=kw.get("overlaps", []),
            notes=kw.get("notes", ""),
            origin=kw.get("origin", "newly-designed"),
        ))

    def other(ctype, dept, slug, purpose, value, trigger, pos, neg, **kw):
        caps.append(Cap(
            id=f"{ctype}.{slug}",
            name=slug,
            department=dept,
            type=ctype,
            purpose=purpose,
            business_value=value,
            trigger=trigger,
            positive=pos,
            negative=neg,
            status=kw.get("status", "implemented"),
            validation=kw.get("validation", "structure-validated"),
            required_credentials=kw.get("required_credentials", []),
            risk_level=kw.get("risk_level", "low"),
            trust_level=kw.get("trust_level", "internal"),
            source=kw.get("source", "internal-reconstruction"),
            source_commit_or_version=kw.get("source_commit_or_version", "company-os-v1"),
            license=kw.get("license", "Apache-2.0"),
            installation_method=kw.get("installation_method", "project-files"),
            overlaps=kw.get("overlaps", []),
            notes=kw.get("notes", ""),
            origin=kw.get("origin", "newly-designed"),
            permissions=kw.get("permissions", ["read-repo"]),
        ))

    # ---- Executive ----
    skill("executive", "strategic-planning",
          "Produce multi-horizon strategic plans with options, trade-offs, and decision criteria.",
          "Aligns company work to outcomes and reduces thrash.",
          "Use when planning strategy, OKRs, initiative portfolios, or quarterly direction.",
          ["Create a 90-day strategy", "Draft OKRs for engineering", "Prioritize company initiatives"],
          ["Implement a React component", "Fix a failing unit test"])
    skill("executive", "decision-brief",
          "Create decision briefs with options, risks, recommendation, and ask.",
          "Speeds executive decisions with comparable options.",
          "Use when a decision needs a concise brief with recommendation.",
          ["Write a go/no-go brief", "Compare build vs buy"],
          ["Write marketing copy", "Run security scan"])
    skill("executive", "initiative-prioritization",
          "Rank initiatives using impact, effort, risk, and dependency scoring.",
          "Focuses scarce capacity on highest-value work.",
          "Use when ranking initiatives, backlog themes, or investment bets.",
          ["Rank these 12 initiatives", "What should we cut this quarter?"],
          ["Debug a flaky test"])
    skill("executive", "status-aggregation",
          "Aggregate department statuses into an executive snapshot with blockers and risks.",
          "Gives leadership a truthful single pane of truth.",
          "Use when producing company status, standup rollups, or weekly exec updates.",
          ["Company status this week", "Aggregate department blockers"],
          ["Design a logo"])
    skill("executive", "risk-escalation",
          "Identify, classify, and escalate cross-cutting risks with owners and mitigations.",
          "Prevents silent failure and late surprises.",
          "Use when risks need escalation paths, severity, and owners.",
          ["Escalate production risk", "Create risk register entry"],
          ["Write SEO metadata"])
    skill("executive", "cross-department-coordination",
          "Coordinate work across departments with RACI, interfaces, and handoffs.",
          "Reduces duplication and dropped interfaces.",
          "Use when multiple departments must collaborate on one initiative.",
          ["Coordinate launch across eng/marketing/cs", "Define RACI for migration"],
          ["Refactor a single module"])
    skill("executive", "completion-review",
          "Verify claimed completion against evidence gates and remaining work.",
          "Stops false-done and incomplete handoffs.",
          "Use when auditing whether work is actually complete.",
          ["Is this feature done?", "Completion audit for the OS build"],
          ["Brainstorm brand names"])
    skill("executive", "executive-reporting",
          "Produce concise executive reports with outcomes, metrics, risks, and asks.",
          "Improves leadership communication quality.",
          "Use when writing exec reports, board-style summaries, or leadership updates.",
          ["Write weekly exec report", "Summarize for leadership"],
          ["Generate TypeScript types"])

    agent("executive", "chief-of-staff",
          "Orchestrate routing, delegation, status aggregation, and completion review.",
          "Provides least-privilege orchestration across departments.",
          "Use for multi-department orchestration and company operating cadence.",
          ["Run company status", "Route this initiative"],
          ["Write raw SQL migrations"],
          ["Read", "Grep", "Glob", "Write"],
          ["Direct production deploys", "Commit secrets", "Bypass security policy"],
          origin="recovered")

    command("executive", "company-status",
            "Produce current company OS status from PROJECT_TRUTH, STATUS, and registries.",
            "Fast truthful status for operators.",
            "Invoke as /company-status",
            ["/company-status", "Show company status"],
            ["Ignore STATUS.md and invent progress"])
    command("executive", "company-plan",
            "Create or refresh a cross-department plan with owners and milestones.",
            "Turns goals into coordinated execution.",
            "Invoke as /company-plan",
            ["/company-plan for Q3 launch"],
            ["Plan without reading ROADMAP"])
    command("executive", "company-health",
            "Assess operating health: registry consistency, validation, security, gaps.",
            "Detects drift before it becomes failure.",
            "Invoke as /company-health",
            ["/company-health"],
            ["Mark health green without running validation"])
    command("executive", "completion-audit",
            "Run completion gates against claimed deliverables.",
            "Evidence-based done criteria.",
            "Invoke as /completion-audit",
            ["/completion-audit wave 7"],
            ["Accept placeholders as complete"])
    command("executive", "generate-handoff",
            "Generate HANDOFF.md from current verified state.",
            "Enables clean continuation.",
            "Invoke as /generate-handoff",
            ["/generate-handoff"],
            ["Overwrite without reading STATUS"])

    # ---- Engineering ----
    for slug, purpose, value, trigger, pos, neg in [
        ("repo-onboarding", "Onboard Claude and humans to an unfamiliar repository with architecture map and risks.",
         "Cuts time-to-productivity and wrong assumptions.",
         "Use when onboarding to a new or unfamiliar codebase.",
         ["Onboard me to this repo", "Map the architecture"], ["Write a sales email"]),
        ("technical-architecture", "Design or review system architecture with constraints, ADRs, and trade-offs.",
         "Prevents costly structural mistakes.",
         "Use for architecture design, ADRs, or system design reviews.",
         ["Design the auth architecture", "Write an ADR"], ["Draft a press release"]),
        ("feature-implementation", "Implement features with tests, incremental commits plan, and verification.",
         "Delivers correct, maintainable code.",
         "Use when implementing product features in code.",
         ["Implement the billing webhook", "Add dark mode toggle"], ["Create a budget forecast"]),
        ("systematic-debugging", "Debug defects with hypothesis, evidence, isolation, and regression tests.",
         "Faster root-cause fixes with less thrash.",
         "Use for bugs, failures, unexpected behavior.",
         ["This endpoint 500s", "Find the race condition"], ["Plan a marketing campaign"]),
        ("safe-refactoring", "Refactor with characterization tests, small steps, and behavior preservation.",
         "Improves structure without regressions.",
         "Use when restructuring code without changing behavior.",
         ["Refactor the payment module", "Extract service layer"], ["Redesign the logo"]),
        ("code-review-skill", "Review diffs for correctness, security, maintainability, and missing tests.",
         "Raises merge quality.",
         "Use when reviewing PRs or local diffs.",
         ["Review this PR", "Code review the auth change"], ["Write Instagram captions"]),
        ("test-generation", "Generate meaningful unit/integration/e2e tests with failure cases.",
         "Improves confidence and catch regressions.",
         "Use when creating or expanding automated tests.",
         ["Generate tests for CheckoutService", "Add negative path tests"], ["Create a pitch deck"]),
        ("webapp-testing", "Plan and execute local webapp testing with reconnaissance then action.",
         "Validates UI flows with evidence.",
         "Use for browser/webapp verification workflows.",
         ["Test the signup flow", "Capture console errors on checkout"], ["Negotiate a contract"],
         ),
        ("api-design", "Design APIs with contracts, versioning, errors, auth, and examples.",
         "Stable interfaces for clients and partners.",
         "Use when designing REST/GraphQL/RPC APIs.",
         ["Design the invoices API", "Define error taxonomy"], ["Write a job description"]),
        ("database-design", "Design schemas, migrations, indexes, and data integrity rules.",
         "Protects data correctness and performance.",
         "Use for schema design, migrations, indexing strategy.",
         ["Design users and orgs schema", "Plan zero-downtime migration"], ["SEO keyword research"]),
        ("dependency-review", "Review dependencies for risk, license, pinning, and alternatives.",
         "Reduces supply-chain and maintenance risk.",
         "Use when adding/updating packages or auditing deps.",
         ["Review these npm packages", "Should we add library X?"], ["Write onboarding email"]),
        ("devops-cicd", "Design CI/CD pipelines, environments, and release automation safely.",
         "Reliable delivery with guardrails.",
         "Use for pipelines, deploy strategy, environment design.",
         ["Design GitHub Actions CI", "Add preview deploys"], ["Draft brand guidelines"]),
        ("release-engineering", "Plan releases with changelogs, rollback, and readiness checks.",
         "Safer production releases.",
         "Use for release planning and cut criteria.",
         ["Prepare v1.2 release", "Write rollback plan"], ["Customer health scoring"]),
        ("technical-documentation", "Write accurate technical docs from code and verified behavior.",
         "Reduces knowledge silos.",
         "Use when documenting systems, APIs, runbooks.",
         ["Document the auth flow", "Write runbook for incidents"], ["Create ad creatives"]),
    ]:
        skill("engineering", slug, purpose, value, trigger, pos, neg,
              origin="recovered" if slug in ("webapp-testing", "repo-onboarding", "code-review-skill") else "newly-designed")

    agent("engineering", "repository-auditor",
          "Audit repository structure, docs, secrets risk, and onboarding readiness.",
          "Finds structural and governance gaps early.",
          "Use for repo audits and onboarding readiness.",
          ["Audit this repository", "Check for missing docs"],
          ["Close a sales deal"],
          ["Read", "Grep", "Glob", "Shell"],
          ["Modify production configs without review", "Commit secrets"])
    agent("engineering", "software-architect",
          "Produce architecture options, ADRs, and constraint analysis.",
          "Improves long-term technical decisions.",
          "Use for architecture work requiring isolated analysis.",
          ["Architecture review for payments", "Propose service boundaries"],
          ["Write cold outreach"],
          ["Read", "Grep", "Glob", "Write"],
          ["Implement large code changes without approval"])
    agent("engineering", "implementation-engineer",
          "Implement approved designs with tests and verification evidence.",
          "Converts plans into working code safely.",
          "Use for isolated implementation workstreams.",
          ["Implement the approved API design"],
          ["Approve legal contracts"],
          ["Read", "Write", "Grep", "Glob", "Shell"],
          ["Disable security controls", "Force push protected branches"])
    agent("engineering", "code-reviewer",
          "Independent code review with severity-ordered findings.",
          "Catches defects before merge.",
          "Use for dedicated review passes.",
          ["Review branch diff", "Security-minded code review"],
          ["Generate marketing landing page"],
          ["Read", "Grep", "Glob", "Shell"],
          ["Approve own unchecked changes", "Merge PRs"])

    for slug, purpose in [
        ("repo-onboard", "Run repository onboarding workflow and produce PROJECT_TRUTH updates."),
        ("architecture-review", "Run architecture review against goals and constraints."),
        ("code-review", "Run structured code review on current changes."),
        ("test-plan", "Produce a test plan with risks and coverage targets."),
        ("run-validation", "Execute Company OS validation suite and summarize results."),
        ("dependency-review", "Review dependency changes and supply-chain risk."),
        ("verified-execution", "Execute a change with explicit verification gates."),
    ]:
        command("engineering", slug, purpose, "Operational engineering workflow.",
                f"Invoke as /{slug}", [f"/{slug}"], [f"Skip verification for /{slug}"])

    # ---- Product ----
    for slug, purpose, value, trigger, pos, neg in [
        ("product-requirements", "Write PRDs with problem, users, requirements, non-goals, metrics.",
         "Aligns build work to user outcomes.", "Use for PRDs and product specs.",
         ["Write a PRD for notifications"], ["Implement CSS"]),
        ("user-stories", "Create user stories with personas, flows, and acceptance hooks.",
         "Makes delivery testable.", "Use when writing user stories.",
         ["Write stories for checkout"], ["Rotate API keys"]),
        ("acceptance-criteria", "Define crisp Given/When/Then and edge-case criteria.",
         "Reduces ambiguous done.", "Use for acceptance criteria and DoD.",
         ["AC for invite flow"], ["Design color palette"]),
        ("product-roadmap", "Build outcome-oriented roadmaps with sequencing and bets.",
         "Communicates direction.", "Use for product roadmaps.",
         ["Draft Q4 roadmap"], ["Fix SQL injection"]),
        ("product-prioritization", "Prioritize using RICE/WSJF/custom scoring with evidence.",
         "Improves portfolio decisions.", "Use for prioritization sessions.",
         ["Prioritize these epics"], ["Write payroll policy"]),
        ("experiment-planning", "Design experiments with hypothesis, metrics, and stop rules.",
         "Reduces vanity experimentation.", "Use for A/B and product experiments.",
         ["Plan experiment for pricing page"], ["Compile TypeScript"]),
        ("product-analytics-planning", "Define product analytics events and success metrics.",
         "Enables learning loops.", "Use for analytics instrumentation planning.",
         ["Define events for onboarding"], ["Negotiate vendor contract"]),
        ("release-planning", "Plan product releases with audiences, risks, and comms.",
         "Coordinates launch readiness.", "Use for product release plans.",
         ["Plan beta release"], ["Tune database indexes"]),
        ("product-review", "Review product artifacts against user value and feasibility.",
         "Catches weak product thinking early.", "Use for product critiques.",
         ["Review this PRD"], ["Generate Kubernetes manifests"]),
    ]:
        skill("product", slug, purpose, value, trigger, pos, neg)

    agent("product", "product-manager",
          "Own requirements, prioritization, and acceptance clarity.",
          "Keeps delivery tied to outcomes.",
          "Use for product definition and review needing isolation.",
          ["Turn this idea into a PRD"], ["Patch production DB"],
          ["Read", "Write", "Grep", "Glob"],
          ["Ship code without engineering review", "Promise legal advice"])
    command("product", "project-truth",
            "Refresh PROJECT_TRUTH.md from verified repository evidence only.",
            "Maintains truthful project state.",
            "Invoke as /project-truth", ["/project-truth"], ["Guess unverified facts"])

    # ---- Design ----
    for slug, purpose, value, trigger, pos, neg in [
        ("ux-research", "Plan and synthesize UX research with methods and bias controls.",
         "Grounds design in user evidence.", "Use for UX research plans/synthesis.",
         ["Plan usability study"], ["Write SQL migration"]),
        ("ui-design", "Produce UI design direction with hierarchy, states, and specs.",
         "Improves usability and clarity.", "Use for UI design tasks.",
         ["Design settings screen"], ["File a patent claim"]),
        ("design-systems", "Extend or review design tokens, components, and usage rules.",
         "Keeps product UI coherent.", "Use for design system work.",
         ["Add toast component tokens"], ["Close books for month"]),
        ("accessibility-review", "Review accessibility against WCAG-oriented checks.",
         "Reduces exclusion and legal risk.", "Use for a11y reviews.",
         ["A11y review this page"], ["Write cold call script"]),
        ("frontend-design", "Apply distinctive, brand-safe frontend design guidance.",
         "Avoids generic AI UI.", "Use when building frontend UI.",
         ["Restyle the landing page"], ["Create payroll forecast"],
         ),
        ("visual-quality-review", "Critique visual quality, hierarchy, and polish.",
         "Raises shipped visual standard.", "Use for visual QA.",
         ["Visual review homepage"], ["Implement OAuth"]),
        ("prototype-planning", "Plan prototypes with fidelity, questions, and success signals.",
         "Speeds learning before build.", "Use for prototype plans.",
         ["Plan clickable prototype"], ["Rotate secrets"]),
        ("brand-application", "Apply brand rules to surfaces without diluting identity.",
         "Protects brand consistency.", "Use for brand application reviews.",
         ["Apply brand to docs site"], ["Debug race condition"]),
    ]:
        skill("design", slug, purpose, value, trigger, pos, neg,
              origin="recovered" if slug == "frontend-design" else "newly-designed")

    agent("design", "design-director",
          "Lead design quality, brand application, and UX coherence.",
          "Protects experience quality.",
          "Use for design direction and reviews.",
          ["Design review for new dashboard"], ["Approve financial statements"],
          ["Read", "Write", "Grep", "Glob"],
          ["Override accessibility requirements", "Invent brand assets as official"])
    command("design", "design-review",
            "Run design and accessibility review workflow.",
            "Structured design critique.",
            "Invoke as /design-review", ["/design-review"], ["Skip a11y checks"])

    # ---- Marketing & Content ----
    for slug, purpose, value, trigger, pos, neg in [
        ("market-research", "Research markets, segments, and demand with sourced claims.",
         "Informs GTM decisions.", "Use for market research.",
         ["Research SMB payroll market"], ["Fix flaky e2e"]),
        ("positioning", "Craft positioning and messaging pillars with proof points.",
         "Clarifies why customers choose you.", "Use for positioning work.",
         ["Position against Competitor X"], ["Migrate Postgres"]),
        ("brand-strategy", "Define brand strategy, personality, and narrative.",
         "Aligns creative and GTM.", "Use for brand strategy.",
         ["Draft brand strategy brief"], ["Write unit tests"]),
        ("campaign-planning", "Plan campaigns with audience, channels, offers, KPIs.",
         "Improves campaign ROI.", "Use for campaign plans.",
         ["Plan launch campaign"], ["Refactor auth module"]),
        ("seo-content", "Plan SEO with intent, structure, and measurement.",
         "Organic acquisition leverage.", "Use for SEO plans/content briefs.",
         ["SEO brief for pricing page"], ["Rotate IAM keys"]),
        ("social-media", "Plan social content with channel norms and brand voice.",
         "Consistent social presence.", "Use for social plans/posts.",
         ["Plan LinkedIn cadence"], ["Design DB indexes"]),
        ("email-marketing", "Write email sequences with goals, segments, and CTAs.",
         "Improves nurture and conversion.", "Use for email marketing.",
         ["Draft onboarding email sequence"], ["Implement WebSocket"]),
        ("copywriting", "Write persuasive, brand-aligned copy for surfaces.",
         "Raises conversion and clarity.", "Use for marketing/product copy.",
         ["Rewrite homepage hero"], ["Security penetration test"]),
        ("editorial-calendar", "Build editorial calendars with themes and owners.",
         "Steady content operations.", "Use for editorial planning.",
         ["Build 30-day editorial calendar"], ["Patch CVE"]),
        ("content-repurposing", "Repurpose long-form into channel-fit assets.",
         "Increases content leverage.", "Use for content repurposing.",
         ["Turn webinar into blog+social"], ["Approve wire transfer"]),
        ("creative-brief", "Write creative briefs with audience, message, constraints.",
         "Improves creative output quality.", "Use for creative briefs.",
         ["Brief for launch video"], ["Tune JVM heap"]),
        ("content-performance", "Review content performance and recommend iterations.",
         "Closes the content learning loop.", "Use for content performance reviews.",
         ["Review blog performance"], ["Create Kubernetes chart"]),
    ]:
        skill("marketing", slug, purpose, value, trigger, pos, neg)

    agent("marketing", "marketing-strategist",
          "Lead market positioning, campaigns, and content strategy.",
          "Connects messaging to growth goals.",
          "Use for GTM/marketing strategy isolation.",
          ["Create GTM plan for new feature"], ["Merge without review"],
          ["Read", "Write", "Grep", "Glob"],
          ["Fabricate metrics", "Impersonate customers"])
    command("marketing", "content-plan",
            "Produce a content/campaign plan with owners and KPIs.",
            "Operational content planning.",
            "Invoke as /content-plan", ["/content-plan"], ["Invent engagement metrics"])
    command("marketing", "market-research",
            "Run sourced market research workflow.",
            "Evidence-based market briefs.",
            "Invoke as /market-research", ["/market-research"], ["Cite unsourced claims as facts"])

    # ---- Sales & CS ----
    for slug, purpose, value, trigger, pos, neg in [
        ("account-research", "Research accounts with org map, pains, and triggers.",
         "Better enterprise conversations.", "Use for account research.",
         ["Research Acme Corp account"], ["Write CSS"]),
        ("prospect-research", "Research prospects and prepare outreach angles.",
         "Raises reply quality.", "Use for prospecting research.",
         ["Research these 5 prospects"], ["Design schema"]),
        ("discovery-prep", "Prepare discovery agendas, questions, and hypotheses.",
         "Improves discovery quality.", "Use for discovery prep.",
         ["Prep discovery for FinTech SMB"], ["Run load test"]),
        ("meeting-prep", "Prepare meeting briefs with goals, risks, and asks.",
         "Sharper customer meetings.", "Use for meeting prep.",
         ["Prep QBR meeting"], ["Bump dependency versions"]),
        ("proposals", "Draft proposals with scope, value, pricing framing, risks.",
         "Faster, clearer commercial docs.", "Use for proposals/SOWs support.",
         ["Draft proposal for analytics package"], ["Implement OAuth"]),
        ("follow-up", "Write follow-ups that advance next steps without pressure spam.",
         "Improves pipeline hygiene.", "Use for sales follow-ups.",
         ["Follow up after demo"], ["Configure CDN"]),
        ("objection-handling", "Prepare objection responses with proof and questions.",
         "Increases win rate.", "Use for objection handling.",
         ["Handle price objection"], ["Write Terraform"]),
        ("pipeline-review", "Review pipeline health, stages, risks, and forecast quality.",
         "Improves forecast integrity.", "Use for pipeline reviews.",
         ["Review pipeline this month"], ["A11y audit icons"]),
        ("customer-onboarding", "Design customer onboarding journeys and success milestones.",
         "Faster time-to-value.", "Use for CS onboarding design.",
         ["Design onboarding for enterprise"], ["Optimize SQL"]),
        ("customer-health", "Assess customer health with signals, risks, plays.",
         "Reduces churn surprises.", "Use for health scoring/reviews.",
         ["Customer health for Acme"], ["Compile Rust"]),
        ("renewal-planning", "Plan renewals with value proof, risks, expansion options.",
         "Protects and grows revenue.", "Use for renewals.",
         ["Plan Acme renewal"], ["Write unit test"]),
        ("cs-reporting", "Produce CS reports with retention, health, and actions.",
         "Makes CS outcomes visible.", "Use for CS reporting.",
         ["Weekly CS report"], ["Design animation"]),
    ]:
        dept = "customer-success" if slug.startswith(("customer-", "renewal-", "cs-")) else "sales"
        skill(dept, slug, purpose, value, trigger, pos, neg)

    agent("sales", "sales-strategist",
          "Prepare account/sales strategy, discovery, and proposals.",
          "Improves commercial readiness.",
          "Use for sales strategy isolation.",
          ["Prepare enterprise pursuit plan"], ["Rotate prod secrets"],
          ["Read", "Write", "Grep", "Glob"],
          ["Guarantee closed revenue", "Misrepresent product capabilities"])
    agent("customer-success", "customer-success-manager",
          "Own onboarding, health, renewal readiness, and CS reporting.",
          "Protects retention and expansion.",
          "Use for CS workflows needing isolation.",
          ["Assess portfolio health"], ["Force push main"],
          ["Read", "Write", "Grep", "Glob"],
          ["Fabricate NPS", "Share customer secrets"])
    command("sales", "sales-brief",
            "Create an account/meeting sales brief.",
            "Ready-to-use sales prep.",
            "Invoke as /sales-brief", ["/sales-brief Acme"], ["Invent customer quotes"])
    command("customer-success", "customer-health",
            "Run customer health assessment workflow.",
            "Actionable health report.",
            "Invoke as /customer-health", ["/customer-health Acme"], ["Ignore churn signals"])
    command("research", "competitor-brief",
            "Produce a sourced competitor brief.",
            "Competitive decision support.",
            "Invoke as /competitor-brief", ["/competitor-brief Contoso"], ["Unsourced competitive claims"])

    # ---- Research ----
    for slug, purpose, value, trigger, pos, neg in [
        ("deep-research", "Conduct deep multi-source research with citation discipline.",
         "High-quality intelligence.", "Use for deep research requests.",
         ["Deep research on edge AI platforms"], ["Rename CSS class"]),
        ("source-verification", "Verify claims against primary sources and note confidence.",
         "Reduces misinformation.", "Use when verifying claims/sources.",
         ["Verify these market size claims"], ["Write jest tests"]),
        ("competitive-intelligence", "Build competitor landscapes with evidence and gaps.",
         "Informs strategy.", "Use for competitive intelligence.",
         ["CI brief on top 3 rivals"], ["Format markdown"]),
        ("trend-analysis", "Analyze trends with time horizon and weak-signal discipline.",
         "Anticipates change.", "Use for trend analysis.",
         ["Trends in agentic tooling"], ["Fix CSS bug"]),
        ("evidence-synthesis", "Synthesize conflicting evidence into calibrated conclusions.",
         "Better decisions under uncertainty.", "Use for evidence synthesis.",
         ["Synthesize conflicting vendor claims"], ["Bump package"]),
        ("regulatory-research", "Research regulations with jurisdiction and disclaimer.",
         "Early compliance awareness—not legal advice.", "Use for regulatory scanning.",
         ["Research SOC2 implications"], ["Design logo"]),
        ("technology-scouting", "Scout technologies with fit, maturity, and risk.",
         "Informs build/buy/adopt.", "Use for tech scouting.",
         ["Scout vector DBs"], ["Write farewell email"]),
        ("research-quality-control", "QA research outputs for sourcing and overclaiming.",
         "Protects research integrity.", "Use for research QC.",
         ["QC this research brief"], ["Implement CRUD"]),
    ]:
        skill("research", slug, purpose, value, trigger, pos, neg)

    agent("research", "research-director",
          "Lead deep research with source standards and synthesis.",
          "Produces decision-grade research.",
          "Use for major research workstreams.",
          ["Lead research on market entry"], ["Deploy to prod"],
          ["Read", "Write", "Grep", "Glob", "WebSearch"],
          ["Present speculation as fact", "Ignore contradictory sources"])
    agent("research", "competitive-intelligence-analyst",
          "Produce competitor briefs and battlecards with evidence.",
          "Supports sales and product strategy.",
          "Use for CI isolation.",
          ["Build competitor battlecard"], ["Approve payroll"],
          ["Read", "Write", "Grep", "Glob", "WebSearch"],
          ["Steal proprietary data", "Fabricate competitor pricing"])
    command("research", "research",
            "Run deep research workflow with source verification.",
            "Structured research package.",
            "Invoke as /research", ["/research agent memory systems"], ["Skip citations"])
    command("research", "source-verify",
            "Verify claims and attach confidence levels.",
            "Claim hygiene.",
            "Invoke as /source-verify", ["/source-verify"], ["Rubber-stamp unverified claims"])

    # ---- Data ----
    for slug, purpose, value, trigger, pos, neg in [
        ("data-quality-analysis", "Assess data quality dimensions and remediation plan.",
         "Trustworthy analytics.", "Use for data quality work.",
         ["Assess CRM data quality"], ["Write jingle"]),
        ("kpi-design", "Design KPI trees with definitions and anti-gaming notes.",
         "Measures what matters.", "Use for KPI design.",
         ["Design activation KPIs"], ["Patch nginx"]),
        ("metric-diagnostics", "Diagnose metric movements with decomposition.",
         "Faster root-cause on KPIs.", "Use when a metric moved unexpectedly.",
         ["Why did conversion drop?"], ["Style a button"]),
        ("dashboard-planning", "Plan dashboards with audience, questions, and definitions.",
         "Useful analytics surfaces.", "Use for dashboard planning.",
         ["Plan exec dashboard"], ["Write Rust FFI"]),
        ("quantitative-analysis", "Perform structured quantitative analysis with assumptions.",
         "Evidence for decisions.", "Use for quantitative analyses.",
         ["Analyze cohort retention"], ["Create brand moodboard"]),
        ("forecasting", "Build forecasts with scenarios and uncertainty ranges.",
         "Planning under uncertainty.", "Use for forecasting.",
         ["Forecast MRR next 2 quarters"], ["A11y icon audit"]),
        ("analytics-report-generation", "Generate analytics reports with charts narrative and caveats.",
         "Clear data storytelling.", "Use for analytics reports.",
         ["Weekly growth report"], ["Negotiate lease"]),
        ("experiment-analysis", "Analyze experiments with validity threats and decisions.",
         "Honest experiment conclusions.", "Use for experiment analysis.",
         ["Analyze pricing A/B"], ["Write Dockerfile"]),
    ]:
        skill("data-analytics", slug, purpose, value, trigger, pos, neg)

    agent("data-analytics", "data-analyst",
          "Analyze metrics, experiments, and data quality with explicit assumptions.",
          "Decision-grade analytics.",
          "Use for analytics isolation.",
          ["Diagnose churn spike"], ["Sign contracts"],
          ["Read", "Write", "Grep", "Glob", "Shell"],
          ["Hide uncertainty", "Present correlation as causation without caveat"])

    # ---- Finance ----
    for slug, purpose, value, trigger, pos, neg in [
        ("budgeting", "Build budgets with drivers, assumptions, and variance framework.",
         "Financial control.", "Use for budgeting support.",
         ["Build eng budget"], ["Write React hook"],
         ),
        ("scenario-planning", "Create financial scenarios with sensitivities.",
         "Stress-tests plans.", "Use for scenario planning.",
         ["Best/base/worst cash scenarios"], ["Fix CSS grid"]),
        ("unit-economics", "Analyze unit economics and contribution margins.",
         "Business model clarity.", "Use for unit economics.",
         ["Analyze CAC/LTV"], ["Design empty state"]),
        ("cash-flow-analysis", "Analyze cash flow timing and runway risks.",
         "Liquidity awareness.", "Use for cash-flow analysis.",
         ["13-week cash flow"], ["Write e2e test"]),
        ("financial-reporting", "Prepare financial narrative reports with caveats.",
         "Transparent finance communication.", "Use for financial reporting support.",
         ["Monthly finance narrative"], ["Ship Docker image"]),
        ("pricing-analysis", "Analyze pricing options with willingness-to-pay proxies.",
         "Better monetization decisions.", "Use for pricing analysis.",
         ["Analyze seat vs usage pricing"], ["Lint Python"]),
        ("investment-evaluation", "Evaluate investments with ROI/NPV framing and risks.",
         "Capital allocation support.", "Use for investment evaluation.",
         ["Evaluate infra investment"], ["Write tweet thread"]),
        ("business-case", "Build business cases with options and decision ask.",
         "Funds the right work.", "Use for business cases.",
         ["Business case for SOC2"], ["Rename variables"]),
    ]:
        skill("finance", slug, purpose, value, trigger, pos, neg,
              safety=["Not a substitute for a licensed financial professional",
                      "Do not invent financial figures",
                      "Label assumptions explicitly"])

    agent("finance", "finance-analyst",
          "Produce financial analyses with assumptions and disclaimers.",
          "Supports planning—not certified advice.",
          "Use for finance analyses isolation.",
          ["Build pricing scenario model"], ["Provide tax filing advice as certified"],
          ["Read", "Write", "Grep", "Glob"],
          ["Present as certified financial advice", "Hide key assumptions"])
    command("finance", "financial-analysis",
            "Run financial analysis workflow with disclaimers.",
            "Structured finance support.",
            "Invoke as /financial-analysis", ["/financial-analysis runway"],
            ["Claim audited accuracy without evidence"])

    # ---- Legal ----
    for slug, purpose, value, trigger, pos, neg in [
        ("legal-issue-spotting", "Spot legal issues and escalation needs—not legal advice.",
         "Earlier risk awareness.", "Use for issue spotting.",
         ["Spot issues in this ToS draft"], ["Optimize images"]),
        ("contract-review-support", "Support contract review with clause checklist and questions.",
         "Prepares counsel conversations.", "Use for contract review support.",
         ["Review NDA checklist"], ["Write CSS animation"]),
        ("policy-analysis", "Analyze policies for gaps, conflicts, and controls.",
         "Stronger internal governance.", "Use for policy analysis.",
         ["Analyze security policy gaps"], ["Design logo mark"]),
        ("compliance-checklists", "Build compliance checklists with evidence mapping.",
         "Audit readiness support.", "Use for compliance checklists.",
         ["SOC2 evidence checklist"], ["Refactor hooks"]),
        ("regulatory-tracking", "Track regulatory changes with jurisdiction tags.",
         "Awareness of external rules.", "Use for regulatory tracking.",
         ["Track AI disclosure rules"], ["Bump eslint"]),
        ("evidence-organization", "Organize compliance/legal evidence with chain of custody notes.",
         "Cleaner audits.", "Use for evidence organization.",
         ["Organize audit evidence"], ["Write marketing slogan"]),
    ]:
        skill("legal-compliance", slug, purpose, value, trigger, pos, neg,
              safety=["Not legal advice", "Escalate to qualified counsel for decisions",
                      "Do not fabricate regulatory citations"])

    agent("legal-compliance", "compliance-reviewer",
          "Review for compliance gaps and escalate legal questions.",
          "Risk reduction support—not counsel.",
          "Use for compliance reviews.",
          ["Compliance check release notes claims"], ["Provide binding legal opinion"],
          ["Read", "Write", "Grep", "Glob"],
          ["Impersonate an attorney", "Give binding legal advice"])
    command("legal-compliance", "compliance-check",
            "Run compliance checklist workflow with escalation notes.",
            "Structured compliance support.",
            "Invoke as /compliance-check", ["/compliance-check"],
            ["Present as legal advice"])

    # ---- Operations ----
    for slug, purpose, value, trigger, pos, neg in [
        ("sop-creation", "Create SOPs with steps, owners, and failure handling.",
         "Repeatable operations.", "Use for SOP creation.",
         ["SOP for incident triage"], ["Write love letter"]),
        ("workflow-design", "Design workflows with queues, SLAs, and interfaces.",
         "Operational clarity.", "Use for workflow design.",
         ["Design intake workflow"], ["Tune SQL"]),
        ("project-management", "Plan projects with milestones, risks, and status cadence.",
         "Delivery predictability.", "Use for PM planning/status.",
         ["Plan migration project"], ["Generate favicon"]),
        ("process-improvement", "Improve processes with waste analysis and pilots.",
         "Efficiency gains.", "Use for process improvement.",
         ["Improve release process"], ["Write poem"]),
        ("vendor-evaluation", "Evaluate vendors with requirements, risks, and TCO.",
         "Better buy decisions.", "Use for vendor evaluation.",
         ["Evaluate CRM vendors"], ["Fix TypeScript error"]),
        ("incident-management", "Run incident process with roles, comms, and postmortems.",
         "Faster recovery and learning.", "Use for incident management.",
         ["Draft incident response SOP"], ["Design business card"]),
        ("handoff-management", "Create operational handoffs with ownership and open risks.",
         "Continuity across people/time.", "Use for handoffs.",
         ["Create sprint handoff"], ["Generate JWT"]),
        ("knowledge-management", "Design knowledge systems and retention practices.",
         "Organizational memory.", "Use for KM design.",
         ["Design wiki IA"], ["Ship hotfix without review"]),
    ]:
        skill("operations", slug, purpose, value, trigger, pos, neg)

    agent("operations", "operations-manager",
          "Own SOPs, workflows, incidents, and operational handoffs.",
          "Keeps the company running.",
          "Use for ops isolation.",
          ["Design release ops workflow"], ["Provide medical advice"],
          ["Read", "Write", "Grep", "Glob"],
          ["Delete production data", "Bypass incident severity rules"])
    command("operations", "process-design",
            "Design or improve an operational process/SOP.",
            "Operational design workflow.",
            "Invoke as /process-design", ["/process-design onboarding"],
            ["Skip failure handling"])

    # ---- HR & Training ----
    for slug, purpose, value, trigger, pos, neg in [
        ("role-design", "Design roles with outcomes, scope, and success signals.",
         "Clearer hiring and performance.", "Use for role design.",
         ["Design Staff Engineer role"], ["Write SQL"]),
        ("hiring-plans", "Create hiring plans with leveling and capacity rationale.",
         "Hiring aligned to strategy.", "Use for hiring plans.",
         ["Hiring plan for platform team"], ["Style navbar"]),
        ("interview-kits", "Build interview kits with scorecards and bias controls.",
         "Fairer hiring signal.", "Use for interview kits.",
         ["Interview kit for PM"], ["Deploy helm chart"]),
        ("employee-onboarding", "Design employee onboarding journeys and checklists.",
         "Faster ramp.", "Use for employee onboarding design.",
         ["30-60-90 onboarding plan"], ["Write regex"]),
        ("training-development", "Design training curricula with objectives and assessments.",
         "Capability building.", "Use for training design.",
         ["Security training curriculum"], ["Negotiate lease"]),
        ("performance-frameworks", "Design performance frameworks with fair criteria.",
         "Aligned growth and feedback.", "Use for performance frameworks.",
         ["Design eng performance rubric"], ["Fix CSS leak"]),
        ("internal-knowledge-systems", "Design internal enablement and knowledge systems.",
         "Scales expertise.", "Use for enablement systems.",
         ["Design internal academy"], ["Bump lockfile"]),
    ]:
        dept = "training" if slug in ("training-development", "internal-knowledge-systems") else "human-resources"
        skill(dept, slug, purpose, value, trigger, pos, neg)

    # ---- Quality & Security ----
    for slug, purpose, value, trigger, pos, neg in [
        ("security-review-skill", "Review changes for security defects and misuse cases.",
         "Reduces vulnerability risk.", "Use for security reviews.",
         ["Security review auth PR"], ["Write haiku"]),
        ("qa-review", "QA review for defects, coverage gaps, and release risk.",
         "Higher release quality.", "Use for QA reviews.",
         ["QA review release candidate"], ["Draft brand manifesto"]),
        ("red-team-review", "Adversarial review of plans/systems for abuse paths.",
         "Finds blind spots.", "Use for red-team style reviews.",
         ["Red-team the invite flow"], ["Write invoice"]),
        ("release-readiness", "Assess release readiness across quality, security, ops.",
         "Safer launches.", "Use for release readiness.",
         ["Release readiness for v2"], [" invent customer logos"]),
        ("permission-audits", "Audit permissions for least privilege and drift.",
         "Access risk reduction.", "Use for permission audits.",
         ["Audit agent permissions"], ["Write jingle"]),
        ("secrets-detection", "Detect credential-like strings and secret handling risks.",
         "Prevents secret leakage.", "Use for secrets scanning workflows.",
         ["Scan for secrets"], ["Design poster"]),
        ("supply-chain-review", "Review supply chain: deps, scripts, provenance.",
         "Third-party risk reduction.", "Use for supply-chain reviews.",
         ["Supply-chain review of install scripts"], ["Write welcome email"]),
        ("governance-enforcement", "Check governance docs/registries match implementation.",
         "Prevents doc drift.", "Use for governance enforcement.",
         ["Enforce registry consistency"], ["Create meme"]),
        ("completion-verification", "Verify completion claims with evidence gates.",
         "Truthful delivery.", "Use for completion verification.",
         ["Verify wave 7 complete"], ["Brainstorm slogans"]),
    ]:
        skill("quality-security", slug, purpose, value, trigger, pos, neg)

    agent("quality-security", "qa-lead",
          "Lead QA strategy, test planning, and release quality gates.",
          "Protects user-facing quality.",
          "Use for QA leadership isolation.",
          ["QA plan for checkout rewrite"], ["Approve unrestricted prod access"],
          ["Read", "Grep", "Glob", "Shell", "Write"],
          ["Skip failing tests silently", "Mark flaky as passing"])
    agent("quality-security", "security-reviewer",
          "Independent security review with severity ordering.",
          "Finds security defects before release.",
          "Use for security review isolation.",
          ["Security review of OAuth change"], ["Ignore high findings"],
          ["Read", "Grep", "Glob", "Shell"],
          ["Disable security controls", "Exfiltrate secrets"])
    agent("quality-security", "completion-auditor",
          "Audit completion claims against registries, tests, and docs.",
          "Blocks false-done.",
          "Use for completion audits.",
          ["Audit Company OS completion"], ["Rubber-stamp incomplete work"],
          ["Read", "Grep", "Glob", "Shell"],
          ["Fabricate test results", "Claim runtime tests that were not run"])
    command("quality-security", "security-review",
            "Run security review workflow.",
            "Structured security findings.",
            "Invoke as /security-review", ["/security-review"], ["Hide critical findings"])
    command("quality-security", "release-readiness",
            "Assess release readiness with evidence.",
            "Go/no-go support.",
            "Invoke as /release-readiness", ["/release-readiness"], ["Ignore open blockers"])
    command("quality-security", "capability-audit",
            "Audit capability registry vs filesystem and statuses.",
            "Registry integrity.",
            "Invoke as /capability-audit", ["/capability-audit"], ["Count placeholders as capabilities"])
    command("quality-security", "capability-search",
            "Search capabilities by department, type, trigger, or status.",
            "Fast capability discovery.",
            "Invoke as /capability-search", ["/capability-search security"], ["Invent unregistered capabilities"])

    # ---- Governing / validation / plugins / MCP / hooks / external / reference ----
    for slug, purpose in [
        ("claude-md", "Repository-wide Claude operating rules."),
        ("company-os-md", "Company structure and routing model."),
        ("project-truth-md", "Verified current project state only."),
        ("status-md", "Implementation and validation status."),
        ("roadmap-md", "Deferred and future work."),
        ("handoff-md", "Continuation instructions."),
        ("security-policy-md", "Secrets, permissions, supply-chain policy."),
        ("changelog-md", "Material environment changes."),
    ]:
        other("governing", "executive", slug, purpose, "Canonical governance.",
              f"Always apply {slug} rules when operating in this repo.",
              [f"Follow {slug}"], [f"Ignore {slug}"], origin="recovered")

    other("validation", "quality-security", "validate-company-os",
          "Primary structural/security validation suite for Company OS.",
          "Deterministic quality gates.",
          "Run via python scripts/validate/validate_company_os.py",
          ["Run full validation"], ["Skip failing checks"],
          origin="newly-designed")
    other("validation", "quality-security", "security-scan",
          "Scan for credential-like strings and unsafe shell patterns.",
          "Security hygiene.",
          "Part of validation suite and scripts/audit.",
          ["Scan secrets"], ["Commit .env"], origin="newly-designed")
    other("validation", "quality-security", "registry-consistency",
          "Ensure registry entries match filesystem artifacts.",
          "Prevents drift.",
          "Validation utility for registries.",
          ["Check registry"], ["Hand-edit registry without validation"], origin="newly-designed")
    other("validation", "quality-security", "trigger-fixture-runner",
          "Evaluate positive/negative trigger fixtures for skills/agents/commands.",
          "Behavioral routing confidence.",
          "tests/*/fixtures and validation suite.",
          ["Run trigger fixtures"], ["Count unread fixtures as passed"], origin="newly-designed")

    other("plugin", "engineering", "anthropic-agent-skills-marketplace",
          "Official Anthropic agent skills marketplace reference.",
          "Access official skills/plugins.",
          "Documented install only after review.",
          ["Add anthropics/skills marketplace"], ["Blind-install all plugins"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/anthropics/skills",
          license="mixed-Apache-and-source-available",
          trust_level="official-anthropic",
          risk_level="medium",
          installation_method="claude-plugin-marketplace",
          notes="Approved with restrictions; not auto-installed in this repo.",
          origin="recovered")
    other("plugin", "engineering", "obra-superpowers",
          "SDLC methodology plugin (planning, TDD, debugging).",
          "Optional process discipline.",
          "Opt-in after hook review.",
          ["Consider superpowers plugin"], ["Force org-wide without review"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/obra/superpowers",
          license="MIT",
          trust_level="community-official-marketplace",
          risk_level="medium",
          installation_method="claude-plugin-opt-in",
          notes="SessionStart hooks may reshape behavior; deferred pending org policy.",
          origin="recovered")
    other("plugin", "engineering", "claude-mem",
          "Persistent memory plugin with local worker.",
          "Optional session memory.",
          "Deferred pending privacy/security review.",
          ["Evaluate claude-mem"], ["Install on shared host without review"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/thedotmack/claude-mem",
          license="Apache-2.0",
          trust_level="community",
          risk_level="high",
          required_credentials=[],
          installation_method="deferred",
          notes="Captures tool output; deferred for security.",
          origin="recovered")

    other("mcp", "engineering", "context7",
          "Up-to-date library documentation MCP.",
          "Accurate third-party docs.",
          "Configure when CONTEXT7_API_KEY available.",
          ["Add Context7 MCP"], ["Send private docs without policy"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/upstash/context7",
          license="MIT-client",
          trust_level="vendor",
          risk_level="medium",
          required_credentials=["CONTEXT7_API_KEY"],
          installation_method="mcp-config-user-local",
          notes="Credential-blocked in this environment; documented only.",
          origin="recovered")
    other("mcp", "engineering", "mcp-builder-skill-ref",
          "Anthropic MCP builder skill as reference for building MCP servers.",
          "Standards for future MCP work.",
          "Reference when authoring MCP servers.",
          ["Design a new MCP server"], ["Expose secrets via MCP"],
          status="approved", validation="source-reviewed",
          source="https://github.com/anthropics/skills/tree/main/skills/mcp-builder",
          license="Apache-2.0",
          trust_level="official-anthropic",
          risk_level="low",
          installation_method="reference-reimplemented-patterns",
          notes="Patterns wrapped into internal docs; not installed as runtime MCP.",
          origin="recovered")

    other("hook", "quality-security", "pre-commit-secrets-hint",
          "Optional documentation for secrets detection before commit.",
          "Prevents accidental secret commits.",
          "Prefer validation script over invasive hooks; hook disabled by default.",
          ["Enable secrets check"], ["Auto-modify git history"],
          status="deferred", validation="source-reviewed",
          risk_level="medium",
          notes="No destructive hooks enabled. Use scripts/validate instead.",
          origin="newly-designed")
    other("hook", "quality-security", "post-validate-registry",
          "Optional post-edit registry consistency check (disabled by default).",
          "Catch registry drift.",
          "Disabled by default; run validate_company_os.py.",
          ["Run registry check"], ["Enable network egress hooks"],
          status="deferred", validation="documented",
          risk_level="low",
          notes="Documented only; not enabled in settings.json.",
          origin="newly-designed")

    other("external", "design", "ui-ux-pro-max",
          "Community UI/UX intelligence skill pack.",
          "Optional design reference.",
          "Do not auto-install; extract curated rules if needed.",
          ["Review ui-ux-pro-max"], ["Vendor entire pack into brand system"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill",
          license="MIT", trust_level="community", risk_level="medium",
          installation_method="deferred",
          notes="Approved with restrictions; reimplemented key principles in frontend-design skill.",
          origin="recovered")
    other("external", "design", "taste-skill",
          "Community anti-slop frontend taste skill.",
          "Optional aesthetic guidance.",
          "Deferred; conflicts possible with brand skill.",
          ["Evaluate taste-skill"], ["Install alongside conflicting UI skills"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/Leonxlnx/taste-skill",
          license="MIT", trust_level="community", risk_level="medium",
          installation_method="deferred", origin="recovered")
    other("external", "design", "transitions-dev",
          "CSS transition snippets and agent skill.",
          "Optional motion references.",
          "Respect no-redistribute license constraints.",
          ["Reference transitions.dev patterns"], ["Redistribute full collection"],
          status="deferred", validation="source-reviewed",
          source="https://github.com/Jakubantalik/transitions.dev",
          license="custom-no-redistribute-collection", trust_level="community",
          risk_level="medium", installation_method="deferred", origin="recovered")
    other("external", "engineering", "skill-creator",
          "Anthropic skill creator for authoring/eval of skills.",
          "Improves skill quality.",
          "Approved reference; patterns used for internal skills.",
          ["Create a new skill"], ["Skip evals"],
          status="approved", validation="source-reviewed",
          source="https://github.com/anthropics/skills",
          license="Apache-2.0", trust_level="official-anthropic", risk_level="low",
          installation_method="reference-patterns", origin="recovered")
    other("external", "engineering", "anthropic-frontend-design",
          "Official frontend design skill patterns.",
          "Baseline UI quality.",
          "Reimplemented internally as frontend-design skill with brand overrides.",
          ["Apply frontend design skill"], ["Ignore brand system"],
          status="implemented", validation="source-reviewed",
          source="https://github.com/anthropics/skills",
          license="Apache-2.0", trust_level="official-anthropic", risk_level="low",
          installation_method="reimplemented-internally", origin="recovered")
    other("external", "engineering", "anthropic-webapp-testing",
          "Official webapp testing skill patterns.",
          "Local web testing discipline.",
          "Reimplemented internally as webapp-testing skill.",
          ["Test webapp flows"], ["Hit production with credentials"],
          status="implemented", validation="source-reviewed",
          source="https://github.com/anthropics/skills",
          license="Apache-2.0", trust_level="official-anthropic", risk_level="low",
          installation_method="reimplemented-internally", origin="recovered")

    other("reference", "executive", "capability-registry",
          "Machine-readable inventory of all capabilities.",
          "Single source for capability truth.",
          "Read registries/CAPABILITY_REGISTRY.yaml",
          ["List capabilities"], ["Add unregistered skill"], origin="newly-designed")
    other("reference", "executive", "source-registry",
          "Inventory of external sources and decisions.",
          "Supply-chain transparency.",
          "Read registries/SOURCE_REGISTRY.md",
          ["Review sources"], ["Install rejected source"], origin="newly-designed")
    other("reference", "quality-security", "testing-guide",
          "How structural vs runtime vs fixture tests are classified.",
          "Honest verification.",
          "docs/testing/",
          ["Classify test evidence"], ["Call static checks runtime tests"], origin="newly-designed")

    return caps


SKILL_TEMPLATE = """---
name: {name}
description: {description}
---

# {title}

## Purpose
{purpose}

## Scope
In scope: {purpose}
Out of scope: work belonging to other departments unless explicitly coordinating.

## Preconditions
- Repository governance documents are readable (`CLAUDE.md`, `COMPANY_OS.md`, `PROJECT_TRUTH.md`).
- Required inputs for the task are available or explicitly marked missing.

## Required context
- Department: `{department}`
- Capability ID: `{id}`
- Related overlaps: {overlaps}

## Required tools
{tools}

## Inputs
- Objective and constraints from the user
- Relevant repository files and prior decisions
- Success criteria or explicit ask

## Ordered workflow
{steps}

## Decision points
- If evidence is missing, stop and request it or mark assumptions.
- If risk is high, escalate via risk-escalation / security-reviewer as appropriate.
- If another department owns the core work, route instead of diluting quality.

## Outputs
{outputs}

## Quality standard
- Evidence-backed claims only
- Explicit assumptions and unknowns
- Actionable next steps with owners when applicable
- No fabricated metrics, citations, or test results

## Safety restrictions
{safety}

## Verification procedure
1. Confirm outputs match the requested objective.
2. Confirm no secrets or credentials were introduced.
3. Confirm overlaps were considered and duplicates avoided.
4. Update STATUS/PROJECT_TRUTH only with verified facts when asked.

## Failure handling
- If blocked on credentials: document as credential-blocked; continue unrelated work.
- If blocked on missing context: produce a partial brief listing gaps.
- If validation fails: do not claim success; file findings.

## Positive examples
{positive}

## Negative examples
{negative}
"""


AGENT_TEMPLATE = """---
name: {name}
description: {description}
tools: {tools_csv}
---

# {title}

## Role
{purpose}

## Responsibilities
- Execute the department specialty with isolated context
- Respect least-privilege tools
- Return structured findings and verification notes
- Escalate risks per SECURITY_POLICY.md

## Delegation criteria
Use this subagent when isolated context, specialized analysis, or restricted tools materially improve outcomes versus inline skill execution.

## Allowed tools
{tools}

## Prohibited actions
{prohibited}

## Required skills
Coordinate with related `{department}` skills registered in `registries/CAPABILITY_REGISTRY.yaml`.

## Input contract
- Objective
- Constraints
- Relevant file paths or artifact references
- Success criteria

## Output contract
- Summary
- Findings (severity ordered when applicable)
- Evidence
- Residual risks
- Recommended next actions

## Escalation rules
- Security issues → security-reviewer / SECURITY_POLICY.md
- Cross-department conflicts → chief-of-staff
- Legal/finance certified advice requests → refuse and escalate to humans

## Verification requirements
- Do not claim runtime success without executed checks
- Cite files and commands used
- Mark credential-blocked items clearly

## Failure handling
Return a blocked/partial report with exact gaps rather than inventing completion.
"""


COMMAND_TEMPLATE = """# /{name}

## Purpose
{purpose}

## Business value
{business_value}

## Invocation
`/{name}`

## Required inputs
- Clear objective (or accept defaults from PROJECT_TRUTH/STATUS when appropriate)
- Any entity names (account, competitor, release) when relevant

## Missing-input behavior
If required inputs are absent, ask for them. If defaults exist in governance docs, state the defaults used.

## Routing
1. Read `PROJECT_TRUTH.md`, `STATUS.md`, and relevant registry entries.
2. Load the matching department skill(s) and/or subagent.
3. Execute the workflow.
4. Write or update only requested artifacts.
5. Report evidence and residual risks.

## Expected output
- Concise result matching the command purpose
- Evidence references
- Next actions
- Explicit status of verification (static / fixture / runtime / credential-blocked)

## Failure handling
- Do not fabricate success
- Document blockers
- Preserve working tree safety (no secrets, no force push, no merge)

## Safety behavior
- Follow SECURITY_POLICY.md
- Least privilege
- No credential printing

## Positive trigger examples
{positive}

## Negative trigger examples
{negative}

## Related capabilities
{overlaps}
"""


def yaml_escape(s: str) -> str:
    if any(c in s for c in [":", "#", "{", "}", "[", "]", ",", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`", "\n"]):
        return json.dumps(s)
    return s


def write_skill(cap: Cap) -> None:
    d = ROOT / ".claude" / "skills" / cap.name
    d.mkdir(parents=True, exist_ok=True)
    (d / "references").mkdir(exist_ok=True)
    (d / "examples").mkdir(exist_ok=True)
    desc = f"{cap.purpose} {cap.trigger} Positive: {'; '.join(cap.positive[:2])}. Negative: {'; '.join(cap.negative[:2])}."
    body = SKILL_TEMPLATE.format(
        name=cap.name,
        description=desc.replace("\n", " "),
        title=cap.name.replace("-", " ").title(),
        purpose=cap.purpose,
        department=cap.department,
        id=cap.id,
        overlaps=", ".join(cap.overlaps) if cap.overlaps else "none",
        tools="\n".join(f"- `{t}`" for t in cap.required_tools),
        steps="\n".join(f"{i+1}. {s}" for i, s in enumerate(cap.workflow_steps)),
        outputs="\n".join(f"- {o}" for o in cap.outputs),
        safety="\n".join(f"- {s}" for s in cap.safety),
        positive="\n".join(f"- {p}" for p in cap.positive),
        negative="\n".join(f"- {n}" for n in cap.negative),
    )
    (d / "SKILL.md").write_text(body, encoding="utf-8")
    (d / "references" / "checklist.md").write_text(
        f"# {cap.name} checklist\n\n- Clarify objective\n- Gather evidence\n- Produce outputs\n- Verify safety\n",
        encoding="utf-8",
    )
    (d / "examples" / "positive.md").write_text(
        "# Positive examples\n\n" + "\n".join(f"- {p}" for p in cap.positive) + "\n",
        encoding="utf-8",
    )
    fixture = {
        "capability_id": cap.id,
        "positive_triggers": cap.positive,
        "negative_triggers": cap.negative,
        "expected_routing": cap.name,
        "expected_output_characteristics": ["structured", "evidence-backed", "safety-aware"],
        "safety_expectation": cap.safety,
        "failure_path_expectation": "Return partial/blocked report without fabricating success",
    }
    tests = ROOT / "tests" / "skills" / cap.name
    tests.mkdir(parents=True, exist_ok=True)
    (tests / "fixtures.json").write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")


def write_agent(cap: Cap) -> None:
    d = ROOT / ".claude" / "agents"
    d.mkdir(parents=True, exist_ok=True)
    tools = cap.allowed_tools or cap.required_tools
    desc = f"{cap.purpose} {cap.trigger}"
    body = AGENT_TEMPLATE.format(
        name=cap.name,
        description=desc.replace("\n", " "),
        tools_csv=", ".join(tools),
        title=cap.name.replace("-", " ").title(),
        purpose=cap.purpose,
        department=cap.department,
        tools="\n".join(f"- `{t}`" for t in tools),
        prohibited="\n".join(f"- {p}" for p in (cap.prohibited or ["Violate SECURITY_POLICY.md"])),
    )
    (d / f"{cap.name}.md").write_text(body, encoding="utf-8")
    tests = ROOT / "tests" / "agents" / cap.name
    tests.mkdir(parents=True, exist_ok=True)
    fixture = {
        "capability_id": cap.id,
        "positive_triggers": cap.positive,
        "negative_triggers": cap.negative,
        "expected_routing": cap.name,
        "allowed_tools": tools,
        "prohibited_actions": cap.prohibited,
        "safety_expectation": ["least-privilege", "no-fabricated-results"],
        "failure_path_expectation": "Blocked/partial report with gaps",
    }
    (tests / "fixtures.json").write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")


def write_command(cap: Cap) -> None:
    d = ROOT / ".claude" / "commands"
    d.mkdir(parents=True, exist_ok=True)
    body = COMMAND_TEMPLATE.format(
        name=cap.name,
        purpose=cap.purpose,
        business_value=cap.business_value,
        positive="\n".join(f"- {p}" for p in cap.positive),
        negative="\n".join(f"- {n}" for n in cap.negative),
        overlaps=", ".join(cap.overlaps) if cap.overlaps else "See CAPABILITY_REGISTRY.yaml",
    )
    (d / f"{cap.name}.md").write_text(body, encoding="utf-8")
    tests = ROOT / "tests" / "commands" / cap.name
    tests.mkdir(parents=True, exist_ok=True)
    fixture = {
        "capability_id": cap.id,
        "invocation": f"/{cap.name}",
        "positive_triggers": cap.positive,
        "negative_triggers": cap.negative,
        "expected_routing": cap.name,
        "missing_input_behavior": "Ask or state defaults from governance docs",
        "safety_expectation": ["no-secrets", "no-fabricated-success"],
        "failure_path_expectation": "Document blockers; do not claim success",
    }
    (tests / "fixtures.json").write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")


def write_dept_readme(dept: str, caps: list[Cap]) -> None:
    path = ROOT / "company" / dept / "README.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {dept.replace('-', ' ').title()} Department",
        "",
        "Capabilities owned by this department:",
        "",
    ]
    for c in caps:
        lines.append(f"- `{c.id}` ({c.type}) — {c.purpose}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_registry(caps: list[Cap]) -> None:
    lines = [
        "# Command Tower Capability Registry",
        f"# Generated: {TODAY}",
        "# status values reflect structural implementation unless noted",
        "version: 1",
        f"generated_on: {TODAY}",
        "capabilities:",
    ]
    for c in caps:
        lines.append(f"  - id: {c.id}")
        lines.append(f"    name: {c.name}")
        lines.append(f"    department: {c.department}")
        lines.append(f"    type: {c.type}")
        lines.append(f"    purpose: {yaml_escape(c.purpose)}")
        lines.append(f"    business_value: {yaml_escape(c.business_value)}")
        lines.append(f"    trigger: {yaml_escape(c.trigger)}")
        lines.append("    positive_trigger_examples:")
        for p in c.positive:
            lines.append(f"      - {yaml_escape(p)}")
        lines.append("    negative_trigger_examples:")
        for n in c.negative:
            lines.append(f"      - {yaml_escape(n)}")
        lines.append(f"    source: {yaml_escape(c.source)}")
        lines.append(f"    source_commit_or_version: {yaml_escape(c.source_commit_or_version)}")
        lines.append(f"    license: {yaml_escape(c.license)}")
        lines.append(f"    trust_level: {c.trust_level}")
        lines.append(f"    installation_method: {c.installation_method}")
        lines.append("    dependencies:")
        for d in c.dependencies or ["none"]:
            lines.append(f"      - {d}")
        lines.append("    required_tools:")
        for t in c.required_tools or ["none"]:
            lines.append(f"      - {t}")
        lines.append("    required_credentials:")
        if c.required_credentials:
            for r in c.required_credentials:
                lines.append(f"      - {r}")
        else:
            lines.append("      - none")
        lines.append("    permissions:")
        for p in c.permissions:
            lines.append(f"      - {p}")
        lines.append(f"    risk_level: {c.risk_level}")
        lines.append(f"    status: {c.status}")
        lines.append(f"    validation: {c.validation}")
        lines.append("    overlaps:")
        for o in c.overlaps or ["none"]:
            lines.append(f"      - {o}")
        lines.append("    supersedes:")
        for s in c.supersedes or ["none"]:
            lines.append(f"      - {s}")
        lines.append(f"    superseded_by: {c.superseded_by or 'none'}")
        lines.append(f"    owner: {c.owner}")
        lines.append(f"    last_reviewed: {TODAY}")
        lines.append(f"    origin: {c.origin}")
        lines.append(f"    notes: {yaml_escape(c.notes or '')}")
    (ROOT / "registries" / "CAPABILITY_REGISTRY.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def md_registry(title: str, types: set[str], path: Path) -> None:
        rows = [c for c in caps if c.type in types]
        out = [f"# {title}", "", f"Count: {len(rows)}", "", "| ID | Name | Department | Status | Purpose |", "|---|---|---|---|---|"]
        for c in rows:
            out.append(f"| `{c.id}` | {c.name} | {c.department} | {c.status} | {c.purpose.replace('|', '/')} |")
        out.append("")
        path.write_text("\n".join(out), encoding="utf-8")

    md_registry("Skill Registry", {"skill"}, ROOT / "registries" / "SKILL_REGISTRY.md")
    md_registry("Agent Registry", {"subagent"}, ROOT / "registries" / "AGENT_REGISTRY.md")
    md_registry("Command Registry", {"command"}, ROOT / "registries" / "COMMAND_REGISTRY.md")
    md_registry("Plugin Registry", {"plugin"}, ROOT / "registries" / "PLUGIN_REGISTRY.md")
    md_registry("MCP Registry", {"mcp"}, ROOT / "registries" / "MCP_REGISTRY.md")
    md_registry("Hook Registry", {"hook"}, ROOT / "registries" / "HOOK_REGISTRY.md")


def main() -> None:
    caps = inventory()
    assert len(caps) >= 100, f"Need 100+ capabilities, got {len(caps)}"

    by_dept: dict[str, list[Cap]] = {}
    for c in caps:
        by_dept.setdefault(c.department, []).append(c)
        if c.type == "skill":
            write_skill(c)
        elif c.type == "subagent":
            write_agent(c)
        elif c.type == "command":
            write_command(c)

    for dept, items in by_dept.items():
        write_dept_readme(dept, items)

    write_registry(caps)

    summary = {
        "total": len(caps),
        "by_type": {},
        "by_department": {k: len(v) for k, v in by_dept.items()},
        "recovered": sum(1 for c in caps if c.origin == "recovered"),
        "newly_designed": sum(1 for c in caps if c.origin == "newly-designed"),
        "implemented": sum(1 for c in caps if c.status == "implemented"),
        "deferred": sum(1 for c in caps if c.status == "deferred"),
        "approved": sum(1 for c in caps if c.status in ("approved", "implemented", "structure-validated")),
    }
    for c in caps:
        summary["by_type"][c.type] = summary["by_type"].get(c.type, 0) + 1

    (ROOT / "registries" / "GENERATION_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
