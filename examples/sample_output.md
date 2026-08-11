# Sample Outputs — CEREBRO Research Agent

> [!WARNING]
> These sample outputs demonstrate retrieval and citation mapping in local evidence-only fallback mode (without LLM synthesis). To demonstrate LLM synthesis, configure `OPENAI_API_KEY` in your `.env` file and run the following command to regenerate:
> `python examples/generate_answers.py`

---

## Question

> What is the annual leave entitlement?

**Insufficient Evidence:** False

**Chunks Retrieved:** 5

## Answer

*Note: LLM is not configured (no OPENAI_API_KEY). Showing extracted evidence passages.*


---

**employee_handbook.txt** — 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t [1]

no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis. 3.2 Leave Carry-Forward Unused annual leave may be carried forward to the next calendar year, subject to a maximum carry-forward of 5 days. Leave exceeding this limit will be forf

## Citations

**[1]** employee_handbook.txt — 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t (Score: 0.888)

> no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave E

**[2]** employee_handbook.txt — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Score: 0.721)

> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks 

**[3]** employee_handbook.txt — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Score: 0.680)

> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ==================================

**[4]** security_policy.txt — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Score: 0.478)

> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software 

**[5]** employee_handbook.txt — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Score: 0.466)

> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10


---

## Question

> How do the leave and remote work policies interact for new employees?

**Insufficient Evidence:** False

**Chunks Retrieved:** 5

## Answer

*Note: LLM is not configured (no OPENAI_API_KEY). Showing extracted evidence passages.*


---

**employee_handbook.txt** — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c [1]

EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across multiple offices globally with a remote-first culture. This handbook outlines the policies, procedures, and guidelines that govern employment at Acme Corp. All employees are expected to read and 

## Citations

**[1]** employee_handbook.txt — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Score: 0.835)

> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ==================================

**[2]** employee_handbook.txt — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Score: 0.716)

> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks 

**[3]** employee_handbook.txt — 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t (Score: 0.644)

> no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave E

**[4]** employee_handbook.txt — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Score: 0.569)

> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10

**[5]** security_policy.txt — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Score: 0.548)

> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software 


---

## Question

> What is the company stock price today?

**Insufficient Evidence:** True

**Chunks Retrieved:** 5

## Answer

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

## Citations

**[1]** security_policy.txt — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Score: 0.723)

> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software 

**[2]** it_support_guide.txt — 2.2 Helpdesk Contact
- Email: itsupport@acmecorp.example.com (response within 4  (Score: 0.460)

> IT SUPPORT AND ONBOARDING GUIDE — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IT-002 | Version 2.0 | Last Updated: January 2025 This is a fictional sample document for demonstration purposes only

**[3]** employee_handbook.txt — 6.2 Anti-Harassment Policy
Acme Corp has a zero-tolerance policy for harassment  (Score: 0.432)

> 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the f

**[4]** employee_handbook.txt — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Score: 0.417)

> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ==================================

**[5]** employee_handbook.txt — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Score: 0.412)

> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10


