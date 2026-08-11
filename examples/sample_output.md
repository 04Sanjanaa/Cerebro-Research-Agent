# Cited Answers — CEREBRO Research Agent

> [!NOTE]
> **Evidence-only fallback mode — LLM synthesis was not executed because OPENAI_API_KEY was unavailable.**
> To demonstrate LLM synthesis, configure `OPENAI_API_KEY` in your `.env` file and run:
> `python examples/generate_answers.py`

---

## Question 1: What is the annual leave entitlement?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 3.1 Annual Leave Entitlement [1]

3.1 Annual Leave Entitlement
Full-time employees are entitled to 20 days of paid annual leave per calendar year.
Leave accrues at a rate of 1.67 days per month of employment.
Part-time employees receive leave on a pro-rata basis.

---

**employee_handbook.txt** — 3.4 Public Holidays [2]

3.4 Public Holidays
Acme Corp observes all nationally recognized public holidays. These days are in
addition to the annual leave entitlement and are not deducted from the leave balance.

---

**employee_handbook.txt** — 3.2 Leave Carry-Forward [3]

3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next calendar year, subject to a
maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited.

---

**employee_handbook.txt** — 3.6 Maternity and Paternity Leave [4]

- Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay)
- Paternity leave: 4 weeks fully paid
- Adoption leave: Same as maternity leave entitlement

---

**employee_handbook.txt** — 3.5 Sick Leave [5]

3.5 Sick Leave
Employees are entitled to 10 days of paid sick leave per year. Sick leave does not
carry forward. Medical certificates are required for absences exceeding 3 consecutive days.

**Grounded:** True

**Relevance Score:** 0.8972

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 3.1 Annual Leave Entitlement (Relevance: Very High - 0.8972)
- **[2] employee_handbook.txt** — Section: 3.4 Public Holidays (Relevance: Very High - 0.8382)
- **[3] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward (Relevance: High - 0.7207)
- **[4] employee_handbook.txt** — Section: 3.6 Maternity and Paternity Leave (Relevance: High - 0.7062)
- **[5] employee_handbook.txt** — Section: 3.5 Sick Leave (Relevance: High - 0.5873)

### Supporting Passages:

#### [1] Excerpt:
> 3.1 Annual Leave Entitlement
Full-time employees are entitled to 20 days of paid annual leave per calendar year.
Leave accrues at a rate of 1.67 days per month of employment.
Part-time employees receive leave on a pro-rata basis.

#### [2] Excerpt:
> 3.4 Public Holidays
Acme Corp observes all nationally recognized public holidays. These days are in
addition to the annual leave entitlement and are not deducted from the leave balance.

#### [3] Excerpt:
> 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next calendar year, subject to a
maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited.

#### [4] Excerpt:
> 3.6 Maternity and Paternity Leave
- Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay)
- Paternity leave: 4 weeks fully paid
- Adoption leave: Same as maternity leave entitlement

#### [5] Excerpt:
> 3.5 Sick Leave
Employees are entitled to 10 days of paid sick leave per year. Sick leave does not
carry forward. Medical certificates are required for absences exceeding 3 consecutive days.

---

## Question 2: How far in advance should leave be requested?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 3.3 Leave Request Procedure [1]

- All leave requests must be submitted at least 14 calendar days (2 weeks) in advance
- Requests must be submitted through the HR Portal at hr-portal.acmecorp.example.com
- Manager approval is required before leave is confirmed
- Emergency leave may be granted with shorter notice subject to manager discretion

---

**employee_handbook.txt** — 3.2 Leave Carry-Forward [2]

3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next calendar year, subject to a
maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited.

---

**employee_handbook.txt** — 3.1 Annual Leave Entitlement [3]

3.1 Annual Leave Entitlement
Full-time employees are entitled to 20 days of paid annual leave per calendar year.
Leave accrues at a rate of 1.67 days per month of employment.
Part-time employees receive leave on a pro-rata basis.

---

**employee_handbook.txt** — 3.6 Maternity and Paternity Leave [4]

- Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay)
- Paternity leave: 4 weeks fully paid
- Adoption leave: Same as maternity leave entitlement

---

**employee_handbook.txt** — 3.5 Sick Leave [5]

3.5 Sick Leave
Employees are entitled to 10 days of paid sick leave per year. Sick leave does not
carry forward. Medical certificates are required for absences exceeding 3 consecutive days.

**Grounded:** True

**Relevance Score:** 0.9006

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 3.3 Leave Request Procedure (Relevance: Very High - 0.9006)
- **[2] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward (Relevance: High - 0.7139)
- **[3] employee_handbook.txt** — Section: 3.1 Annual Leave Entitlement (Relevance: High - 0.6779)
- **[4] employee_handbook.txt** — Section: 3.6 Maternity and Paternity Leave (Relevance: High - 0.6692)
- **[5] employee_handbook.txt** — Section: 3.5 Sick Leave (Relevance: High - 0.6588)

### Supporting Passages:

#### [1] Excerpt:
> 3.3 Leave Request Procedure
- All leave requests must be submitted at least 14 calendar days (2 weeks) in advance
- Requests must be submitted through the HR Portal at hr-portal.acmecorp.example.com
- Manager approval is required before leave is confirmed
- Emergency leave may be granted with shorter notice subject to manager discretion

#### [2] Excerpt:
> 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next calendar year, subject to a
maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited.

#### [3] Excerpt:
> 3.1 Annual Leave Entitlement
Full-time employees are entitled to 20 days of paid annual leave per calendar year.
Leave accrues at a rate of 1.67 days per month of employment.
Part-time employees receive leave on a pro-rata basis.

#### [4] Excerpt:
> 3.6 Maternity and Paternity Leave
- Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay)
- Paternity leave: 4 weeks fully paid
- Adoption leave: Same as maternity leave entitlement

#### [5] Excerpt:
> 3.5 Sick Leave
Employees are entitled to 10 days of paid sick leave per year. Sick leave does not
carry forward. Medical certificates are required for absences exceeding 3 consecutive days.

---

## Question 3: What is the remote work policy?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.3 Fully Remote Work [1]

- Department head approval
- Demonstrated 6+ months of successful hybrid work
- Role classification as remote-eligible by HR
- Annual review and reconfirmation

---

**employee_handbook.txt** — 4.1 Eligibility Requirements [2]

- Successfully completed the 90-day probationary period
- Role has been assessed as suitable for remote work by their manager
- No active performance improvement plans (PIPs)
- Manager approval obtained in writing

---

**employee_handbook.txt** — 4.2 Hybrid Work Schedule [3]

4.2 Hybrid Work Schedule
Eligible employees may work remotely up to 3 days per week under the hybrid model.
The remaining 2 days must be spent in the office unless otherwise agreed.

---

**employee_handbook.txt** — 2.2 Probationary Period [4]

- Performance is closely monitored
- Benefits eligibility may be limited (see Section 5)
- Remote work is not permitted (see Section 4)
- Employment may be terminated without notice

---

**security_policy.txt** — 5.1 What to Report [5]

- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

**Grounded:** True

**Relevance Score:** 0.8959

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.3 Fully Remote Work (Relevance: Very High - 0.8959)
- **[2] employee_handbook.txt** — Section: 4.1 Eligibility Requirements (Relevance: Very High - 0.8212)
- **[3] employee_handbook.txt** — Section: 4.2 Hybrid Work Schedule (Relevance: High - 0.7390)
- **[4] employee_handbook.txt** — Section: 2.2 Probationary Period (Relevance: High - 0.6686)
- **[5] security_policy.txt** — Section: 5.1 What to Report (Relevance: High - 0.6364)

### Supporting Passages:

#### [1] Excerpt:
> 4.3 Fully Remote Work
Fully remote work (5 days per week from home) is subject to:
- Department head approval
- Demonstrated 6+ months of successful hybrid work
- Role classification as remote-eligible by HR
- Annual review and reconfirmation

#### [2] Excerpt:
> 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria to be eligible for remote work:
- Successfully completed the 90-day probationary period
- Role has been assessed as suitable for remote work by their manager
- No active performance improvement plans (PIPs)
- Manager approval obtained in writing

#### [3] Excerpt:
> 4.2 Hybrid Work Schedule
Eligible employees may work remotely up to 3 days per week under the hybrid model.
The remaining 2 days must be spent in the office unless otherwise agreed.

#### [4] Excerpt:
> 2.2 Probationary Period
All new employees serve a 90-day probationary period. During this period:
- Performance is closely monitored
- Benefits eligibility may be limited (see Section 5)
- Remote work is not permitted (see Section 4)
- Employment may be terminated without notice

#### [5] Excerpt:
> 5.1 What to Report
Employees must report the following immediately:
- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

---

## Question 4: What are the password requirements?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**security_policy.txt** — 2.1 Password Complexity [1]

- Minimum length: 12 characters
- Must include at least one uppercase letter (A-Z)
- Must include at least one lowercase letter (a-z)
- Must include at least one number (0-9)
- Must include at least one special character (!@#$%^&*)
- Must not contain the user's name, email address, or username
- Must not be a previously used password (last 12 passwords are blocked)

---

**it_support_guide.txt** — 4.3 Password Reset [2]

4.3 Password Reset
Self-service password reset available at: password-reset.acmecorp.example.com
Requires MFA verification and answers to security questions.

---

**security_policy.txt** — 5.1 What to Report [3]

- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

---

**it_support_guide.txt** — 2.1 Self-Service Portal [4]

- Password resets
- Software installation requests
- Account unlock requests
- Common troubleshooting guides

---

**security_policy.txt** — 2.2 Password Expiry [5]

2.2 Password Expiry
Passwords must be changed every 90 days. Users will receive a reminder 14 days before expiry.
Failure to update passwords will result in account lockout.

**Grounded:** True

**Relevance Score:** 0.9121

### Sources Cited:

- **[1] security_policy.txt** — Section: 2.1 Password Complexity (Relevance: Very High - 0.9121)
- **[2] it_support_guide.txt** — Section: 4.3 Password Reset (Relevance: High - 0.7133)
- **[3] security_policy.txt** — Section: 5.1 What to Report (Relevance: High - 0.6692)
- **[4] it_support_guide.txt** — Section: 2.1 Self-Service Portal (Relevance: High - 0.6131)
- **[5] security_policy.txt** — Section: 2.2 Password Expiry (Relevance: High - 0.6082)

### Supporting Passages:

#### [1] Excerpt:
> 2.1 Password Complexity
All user account passwords must meet the following requirements:
- Minimum length: 12 characters
- Must include at least one uppercase letter (A-Z)
- Must include at least one lowercase letter (a-z)
- Must include at least one number (0-9)
- Must include at least one special character (!@#$%^&*)
- Must not contain the user's name, email address, or username
- Must not be a...

#### [2] Excerpt:
> 4.3 Password Reset
Self-service password reset available at: password-reset.acmecorp.example.com
Requires MFA verification and answers to security questions.

#### [3] Excerpt:
> 5.1 What to Report
Employees must report the following immediately:
- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

#### [4] Excerpt:
> 2.1 Self-Service Portal
Access the IT Self-Service Portal at: it-support.acmecorp.example.com
Available 24/7 for:
- Password resets
- Software installation requests
- Account unlock requests
- Common troubleshooting guides

#### [5] Excerpt:
> 2.2 Password Expiry
Passwords must be changed every 90 days. Users will receive a reminder 14 days before expiry.
Failure to update passwords will result in account lockout.

---

## Question 5: What are the main requirements for working remotely?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.1 Eligibility Requirements [1]

- Successfully completed the 90-day probationary period
- Role has been assessed as suitable for remote work by their manager
- No active performance improvement plans (PIPs)
- Manager approval obtained in writing

---

**employee_handbook.txt** — 4.2 Hybrid Work Schedule [2]

4.2 Hybrid Work Schedule
Eligible employees may work remotely up to 3 days per week under the hybrid model.
The remaining 2 days must be spent in the office unless otherwise agreed.

---

**employee_handbook.txt** — 4.6 In-Office Requirements [3]

- All-hands meetings and town halls
- Quarterly performance reviews
- Team-building events designated as mandatory
- Client meetings requiring physical presence

---

**security_policy.txt** — 6.2 Home Network Security [4]

- Home Wi-Fi router uses WPA3 or WPA2 encryption
- Router firmware is kept up to date
- Guest network is separate from the working network

---

**security_policy.txt** — 5.1 What to Report [5]

- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

**Grounded:** True

**Relevance Score:** 0.7975

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.1 Eligibility Requirements (Relevance: Very High - 0.7975)
- **[2] employee_handbook.txt** — Section: 4.2 Hybrid Work Schedule (Relevance: Very High - 0.7851)
- **[3] employee_handbook.txt** — Section: 4.6 In-Office Requirements (Relevance: Very High - 0.7578)
- **[4] security_policy.txt** — Section: 6.2 Home Network Security (Relevance: High - 0.7368)
- **[5] security_policy.txt** — Section: 5.1 What to Report (Relevance: High - 0.7343)

### Supporting Passages:

#### [1] Excerpt:
> 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria to be eligible for remote work:
- Successfully completed the 90-day probationary period
- Role has been assessed as suitable for remote work by their manager
- No active performance improvement plans (PIPs)
- Manager approval obtained in writing

#### [2] Excerpt:
> 4.2 Hybrid Work Schedule
Eligible employees may work remotely up to 3 days per week under the hybrid model.
The remaining 2 days must be spent in the office unless otherwise agreed.

#### [3] Excerpt:
> 4.6 In-Office Requirements
Even while on a remote schedule, employees must attend the office for:
- All-hands meetings and town halls
- Quarterly performance reviews
- Team-building events designated as mandatory
- Client meetings requiring physical presence

#### [4] Excerpt:
> 6.2 Home Network Security
Remote workers must ensure:
- Home Wi-Fi router uses WPA3 or WPA2 encryption
- Router firmware is kept up to date
- Guest network is separate from the working network

#### [5] Excerpt:
> 5.1 What to Report
Employees must report the following immediately:
- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

---

## Question 6: How do the leave and remote work policies relate to each other?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.3 Fully Remote Work [1]

- Department head approval
- Demonstrated 6+ months of successful hybrid work
- Role classification as remote-eligible by HR
- Annual review and reconfirmation

---

**employee_handbook.txt** [2]

Acme Corp is a technology services company founded in 2005. We operate across
multiple offices globally with a remote-first culture. This handbook outlines
the policies, procedures, and guidelines that govern employment at Acme Corp.
All employees are expected to read and comply with the policies described herein.
Questions should be directed to Human Resources at hr@acmecorp.example.com.

---

**employee_handbook.txt** — 4.1 Eligibility Requirements [3]

- Successfully completed the 90-day probationary period
- Role has been assessed as suitable for remote work by their manager
- No active performance improvement plans (PIPs)
- Manager approval obtained in writing

---

**employee_handbook.txt** — 4.2 Hybrid Work Schedule [4]

4.2 Hybrid Work Schedule
Eligible employees may work remotely up to 3 days per week under the hybrid model.
The remaining 2 days must be spent in the office unless otherwise agreed.

---

**employee_handbook.txt** — 3.6 Maternity and Paternity Leave [5]

- Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay)
- Paternity leave: 4 weeks fully paid
- Adoption leave: Same as maternity leave entitlement

**Grounded:** True

**Relevance Score:** 0.8668

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.3 Fully Remote Work (Relevance: Very High - 0.8668)
- **[2] employee_handbook.txt** — Section:  (Relevance: Very High - 0.7779)
- **[3] employee_handbook.txt** — Section: 4.1 Eligibility Requirements (Relevance: Very High - 0.7539)
- **[4] employee_handbook.txt** — Section: 4.2 Hybrid Work Schedule (Relevance: High - 0.7046)
- **[5] employee_handbook.txt** — Section: 3.6 Maternity and Paternity Leave (Relevance: High - 0.6809)

### Supporting Passages:

#### [1] Excerpt:
> 4.3 Fully Remote Work
Fully remote work (5 days per week from home) is subject to:
- Department head approval
- Demonstrated 6+ months of successful hybrid work
- Role classification as remote-eligible by HR
- Annual review and reconfirmation

#### [2] Excerpt:
> Acme Corp is a technology services company founded in 2005. We operate across
multiple offices globally with a remote-first culture. This handbook outlines
the policies, procedures, and guidelines that govern employment at Acme Corp.

All employees are expected to read and comply with the policies described herein.
Questions should be directed to Human Resources at hr@acmecorp.example.com.

#### [3] Excerpt:
> 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria to be eligible for remote work:
- Successfully completed the 90-day probationary period
- Role has been assessed as suitable for remote work by their manager
- No active performance improvement plans (PIPs)
- Manager approval obtained in writing

#### [4] Excerpt:
> 4.2 Hybrid Work Schedule
Eligible employees may work remotely up to 3 days per week under the hybrid model.
The remaining 2 days must be spent in the office unless otherwise agreed.

#### [5] Excerpt:
> 3.6 Maternity and Paternity Leave
- Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay)
- Paternity leave: 4 weeks fully paid
- Adoption leave: Same as maternity leave entitlement

---

## Question 7: What are the main employee responsibilities described in the policies?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** [1]

Acme Corp is a technology services company founded in 2005. We operate across
multiple offices globally with a remote-first culture. This handbook outlines
the policies, procedures, and guidelines that govern employment at Acme Corp.
All employees are expected to read and comply with the policies described herein.
Questions should be directed to Human Resources at hr@acmecorp.example.com.

---

**employee_handbook.txt** — 5.3 Health Insurance [2]

5.3 Health Insurance
Acme Corp provides comprehensive health insurance for all full-time employees.
Coverage begins on the first day of the month following the start date.
Dependents may be added to the plan at the employee's expense.

---

**security_policy.txt** — 5.1 What to Report [3]

- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

---

**security_policy.txt** — 4.1 Company Equipment [4]

- Involve illegal activities
- Compromise system security
- Consume excessive network resources
- Interfere with work responsibilities

---

**employee_handbook.txt** — 3.4 Public Holidays [5]

3.4 Public Holidays
Acme Corp observes all nationally recognized public holidays. These days are in
addition to the annual leave entitlement and are not deducted from the leave balance.

**Grounded:** True

**Relevance Score:** 0.7983

### Sources Cited:

- **[1] employee_handbook.txt** — Section:  (Relevance: Very High - 0.7983)
- **[2] employee_handbook.txt** — Section: 5.3 Health Insurance (Relevance: High - 0.6171)
- **[3] security_policy.txt** — Section: 5.1 What to Report (Relevance: High - 0.6090)
- **[4] security_policy.txt** — Section: 4.1 Company Equipment (Relevance: High - 0.5579)
- **[5] employee_handbook.txt** — Section: 3.4 Public Holidays (Relevance: Medium - 0.5402)

### Supporting Passages:

#### [1] Excerpt:
> Acme Corp is a technology services company founded in 2005. We operate across
multiple offices globally with a remote-first culture. This handbook outlines
the policies, procedures, and guidelines that govern employment at Acme Corp.

All employees are expected to read and comply with the policies described herein.
Questions should be directed to Human Resources at hr@acmecorp.example.com.

#### [2] Excerpt:
> 5.3 Health Insurance
Acme Corp provides comprehensive health insurance for all full-time employees.
Coverage begins on the first day of the month following the start date.
Dependents may be added to the plan at the employee's expense.

#### [3] Excerpt:
> 5.1 What to Report
Employees must report the following immediately:
- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

#### [4] Excerpt:
> 4.1 Company Equipment
Company-provided equipment must be used primarily for business purposes.
Limited personal use is permitted provided it does not:
- Involve illegal activities
- Compromise system security
- Consume excessive network resources
- Interfere with work responsibilities

#### [5] Excerpt:
> 3.4 Public Holidays
Acme Corp observes all nationally recognized public holidays. These days are in
addition to the annual leave entitlement and are not deducted from the leave balance.

---

## Question 8: What was the company's revenue last year?

**Answer:**

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

**Grounded:** False

**Relevance Score:** 0.7312

### Sources Cited:

- **[1] security_policy.txt** — Section: 5.1 What to Report (Relevance: High - 0.7312)
- **[2] employee_handbook.txt** — Section: 5.2 Performance Bonus (Relevance: High - 0.5902)
- **[3] employee_handbook.txt** — Section: 4.5 Equipment and Internet Requirements (Relevance: High - 0.5765)
- **[4] expense_policy.txt** — Section: 2.3 Professional Development (Relevance: High - 0.5566)
- **[5] expense_policy.txt** — Section: EXPENSE REIMBURSEMENT POLICY — ACME CORP (SAMPLE / FICTIONAL) (Relevance: High - 0.5527)

### Supporting Passages:

#### [1] Excerpt:
> 5.1 What to Report
Employees must report the following immediately:
- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

#### [2] Excerpt:
> 5.2 Performance Bonus
Eligible employees may receive an annual performance bonus of up to 15% of base salary,
awarded in April based on the prior year's performance.

#### [3] Excerpt:
> 4.5 Equipment and Internet Requirements
- Stable internet connection with minimum download speed of 50 Mbps is required
- Employees must have a dedicated workspace free from distractions
- Company-provided laptop must be used for all work activities
- Personal home office stipend: $500 USD per year (reimbursed via expense portal)

#### [4] Excerpt:
> 2.3 Professional Development
- Conference registration fees: Up to $2,000 per conference with manager approval
- Training courses or certifications: Up to $1,500 per year without additional approval
- Books and subscriptions directly related to role: Up to $200 per year

#### [5] Excerpt:
> EXPENSE REIMBURSEMENT POLICY — ACME CORP (SAMPLE / FICTIONAL)
Policy Reference: FIN-003 | Version 1.8 | Last Updated: February 2025
This is a fictional sample document for demonstration purposes only.

---

## Question 9: Who is the company's CEO?

**Answer:**

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

**Grounded:** False

**Relevance Score:** 0.7390

### Sources Cited:

- **[1] security_policy.txt** — Section:  (Relevance: High - 0.7390)
- **[2] expense_policy.txt** — Section: 5.1 Eligibility (Relevance: High - 0.6059)
- **[3] security_policy.txt** — Section: 6.1 VPN Requirement (Relevance: High - 0.5648)
- **[4] expense_policy.txt** — Section:  (Relevance: Medium - 0.5412)
- **[5] employee_handbook.txt** — Section: 5.4 Retirement Plan (Relevance: Medium - 0.5360)

### Supporting Passages:

#### [1] Excerpt:
> This policy establishes the information security requirements for all Acme Corp
employees, contractors, and third-party users who access company systems or data.
Non-compliance may result in disciplinary action up to and including termination.

#### [2] Excerpt:
> 5.1 Eligibility
Corporate credit cards are issued to employees who travel more than 4 times per year.
Applications must be approved by Finance and HR.

#### [3] Excerpt:
> 6.1 VPN Requirement
All remote access to company systems must be through the corporate VPN.
Direct access to internal systems from the public internet is prohibited.

#### [4] Excerpt:
> This policy governs the reimbursement of business-related expenses incurred by
Acme Corp employees. All expenses must be legitimate, reasonable, and directly
related to company business.

#### [5] Excerpt:
> 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 months of employment.
Acme Corp matches contributions up to 4% of base salary.

---

## Question 10: What is the company's stock price today?

**Answer:**

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

**Grounded:** False

**Relevance Score:** 0.7184

### Sources Cited:

- **[1] security_policy.txt** — Section: 5.1 What to Report (Relevance: High - 0.7184)
- **[2] security_policy.txt** — Section: 6.1 VPN Requirement (Relevance: Medium - 0.5264)
- **[3] it_support_guide.txt** — Section: 1.1 Pre-Start Setup (1 Week Before) (Relevance: Medium - 0.4998)
- **[4] employee_handbook.txt** — Section: 5.4 Retirement Plan (Relevance: Medium - 0.4929)
- **[5] expense_policy.txt** — Section:  (Relevance: Medium - 0.4924)

### Supporting Passages:

#### [1] Excerpt:
> 5.1 What to Report
Employees must report the following immediately:
- Lost or stolen company devices
- Suspected phishing emails or social engineering attempts
- Unauthorized access to systems or data
- Data breaches or accidental data disclosure

#### [2] Excerpt:
> 6.1 VPN Requirement
All remote access to company systems must be through the corporate VPN.
Direct access to internal systems from the public internet is prohibited.

#### [3] Excerpt:
> 1.1 Pre-Start Setup (1 Week Before)
Before your start date, IT will:
- Provision your company laptop (Dell XPS or MacBook Pro depending on role)
- Create your company email account (firstname.lastname@acmecorp.example.com)
- Set up your accounts for Microsoft 365, Slack, and the HR Portal
- Send setup credentials to your personal email address

#### [4] Excerpt:
> 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 months of employment.
Acme Corp matches contributions up to 4% of base salary.

#### [5] Excerpt:
> This policy governs the reimbursement of business-related expenses incurred by
Acme Corp employees. All expenses must be legitimate, reasonable, and directly
related to company business.

---

