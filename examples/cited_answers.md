# Cited Answers — CEREBRO Research Agent

> [!WARNING]
> These sample outputs demonstrate retrieval and citation mapping in local evidence-only fallback mode (without LLM synthesis). To demonstrate LLM synthesis, configure `OPENAI_API_KEY` in your `.env` file and run the following command to regenerate:
> `python examples/generate_answers.py`

---
## Question 1: What is the annual leave entitlement?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t [1]

no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis. 3.2 Leave Carry-Forward Unused annual leave may be carried forward to the next calendar year, subject to a maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited. 3.3 Leave Request Procedure - All leave requests must be submitted at least 14 calendar days (2 weeks) in advance - Requests must be submitted through the HR Portal at hr-portal.acmecorp.example.com - Manager approval is required before leave is confirmed - Emergency leave may be granted with shorter notice subject to manager discretion 3.4 Public Holidays Acme Corp observes all nationally recognized public holidays. These days are in addition to the annual leave entitlement and are not deducted from the leave balance. 3.5 Sick Leave Employees are entitled to 10 days of paid sick leave per year. Sick leave does not carry forward. Medical certificates are required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY =============================================================

---

**employee_handbook.txt** — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu [2]

required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ============================================================= 4.1 Eligibility Requirements Employees must meet ALL of the following criteria to be eligible for remote work: - Successfully completed the 90-day probationary period - Role has been assessed as suitable for remote work by their manager - No active performance improvement plans (PIPs) - Manager approval obtained in writing 4.2 Hybrid Work Schedule Eligible employees may work remotely up to 3 days per week under the hybrid model. The remaining 2 days must be spent in the office unless otherwise agreed. 4.3 Fully Remote Work Fully remote work (5 days per week from home) is subject to: - Department head approval - Demonstrated 6+ months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours.

---

**employee_handbook.txt** — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c [3]

EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across multiple offices globally with a remote-first culture. This handbook outlines the policies, procedures, and guidelines that govern employment at Acme Corp. All employees are expected to read and comply with the policies described herein. Questions should be directed to Human Resources at hr@acmecorp.example.com. ============================================================= SECTION 2: EMPLOYMENT POLICIES ============================================================= 2.1 Equal Opportunity Employment Acme Corp is an equal opportunity employer. We do not discriminate on the basis of race, color, religion, gender, national origin, age, disability, or any other protected characteristic. 2.2 Probationary Period All new employees serve a 90-day probationary period. During this period: - Performance is closely monitored - Benefits eligibility may be limited (see Section 5) - Remote work is not permitted (see Section 4) - Employment may be terminated without notice 2.3 Employment Classifications - Full-time: 40 hours per week, eligible for all benefits - Part-time: Less than 30 hours per week, limited benefits - Contract: Project-based, no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis.

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [4]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**employee_handbook.txt** — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m [5]

months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum download speed of 50 Mbps is required - Employees must have a dedicated workspace free from distractions - Company-provided laptop must be used for all work activities - Personal home office stipend: $500 USD per year (reimbursed via expense portal) 4.6 In-Office Requirements Even while on a remote schedule, employees must attend the office for: - All-hands meetings and town halls - Quarterly performance reviews - Team-building events designated as mandatory - Client meetings requiring physical presence ============================================================= SECTION 5: COMPENSATION AND BENEFITS ============================================================= 5.1 Salary Review Salary reviews are conducted annually in March. Merit increases are based on performance ratings and company financial performance. 5.2 Performance Bonus Eligible employees may receive an annual performance bonus of up to 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense.

**Grounded:** True

**Relevance Score:** 0.8882

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t (Relevance: Very High - 0.8882)
- **[2] employee_handbook.txt** — Section: 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Relevance: High - 0.7206)
- **[3] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Relevance: High - 0.6799)
- **[4] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: Medium - 0.4783)
- **[5] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: Medium - 0.4657)

### Supporting Passages:

#### [1] Excerpt:
> no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-...

#### [2] Excerpt:
> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ===========================================...

#### [3] Excerpt:
> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across mult...

#### [4] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [5] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

---

## Question 2: How far in advance should leave be requested?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t [1]

no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis. 3.2 Leave Carry-Forward Unused annual leave may be carried forward to the next calendar year, subject to a maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited. 3.3 Leave Request Procedure - All leave requests must be submitted at least 14 calendar days (2 weeks) in advance - Requests must be submitted through the HR Portal at hr-portal.acmecorp.example.com - Manager approval is required before leave is confirmed - Emergency leave may be granted with shorter notice subject to manager discretion 3.4 Public Holidays Acme Corp observes all nationally recognized public holidays. These days are in addition to the annual leave entitlement and are not deducted from the leave balance. 3.5 Sick Leave Employees are entitled to 10 days of paid sick leave per year. Sick leave does not carry forward. Medical certificates are required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY =============================================================

---

**employee_handbook.txt** — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c [2]

EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across multiple offices globally with a remote-first culture. This handbook outlines the policies, procedures, and guidelines that govern employment at Acme Corp. All employees are expected to read and comply with the policies described herein. Questions should be directed to Human Resources at hr@acmecorp.example.com. ============================================================= SECTION 2: EMPLOYMENT POLICIES ============================================================= 2.1 Equal Opportunity Employment Acme Corp is an equal opportunity employer. We do not discriminate on the basis of race, color, religion, gender, national origin, age, disability, or any other protected characteristic. 2.2 Probationary Period All new employees serve a 90-day probationary period. During this period: - Performance is closely monitored - Benefits eligibility may be limited (see Section 5) - Remote work is not permitted (see Section 4) - Employment may be terminated without notice 2.3 Employment Classifications - Full-time: 40 hours per week, eligible for all benefits - Part-time: Less than 30 hours per week, limited benefits - Contract: Project-based, no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis.

---

**employee_handbook.txt** — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu [3]

required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ============================================================= 4.1 Eligibility Requirements Employees must meet ALL of the following criteria to be eligible for remote work: - Successfully completed the 90-day probationary period - Role has been assessed as suitable for remote work by their manager - No active performance improvement plans (PIPs) - Manager approval obtained in writing 4.2 Hybrid Work Schedule Eligible employees may work remotely up to 3 days per week under the hybrid model. The remaining 2 days must be spent in the office unless otherwise agreed. 4.3 Fully Remote Work Fully remote work (5 days per week from home) is subject to: - Department head approval - Demonstrated 6+ months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours.

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [4]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**employee_handbook.txt** — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m [5]

months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum download speed of 50 Mbps is required - Employees must have a dedicated workspace free from distractions - Company-provided laptop must be used for all work activities - Personal home office stipend: $500 USD per year (reimbursed via expense portal) 4.6 In-Office Requirements Even while on a remote schedule, employees must attend the office for: - All-hands meetings and town halls - Quarterly performance reviews - Team-building events designated as mandatory - Client meetings requiring physical presence ============================================================= SECTION 5: COMPENSATION AND BENEFITS ============================================================= 5.1 Salary Review Salary reviews are conducted annually in March. Merit increases are based on performance ratings and company financial performance. 5.2 Performance Bonus Eligible employees may receive an annual performance bonus of up to 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense.

**Grounded:** True

**Relevance Score:** 0.8753

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t (Relevance: Very High - 0.8753)
- **[2] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Relevance: High - 0.7095)
- **[3] employee_handbook.txt** — Section: 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Relevance: High - 0.6267)
- **[4] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: Medium - 0.4963)
- **[5] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: Low - 0.3883)

### Supporting Passages:

#### [1] Excerpt:
> no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-...

#### [2] Excerpt:
> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across mult...

#### [3] Excerpt:
> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ===========================================...

#### [4] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [5] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

---

## Question 3: What is the remote work policy?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu [1]

required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ============================================================= 4.1 Eligibility Requirements Employees must meet ALL of the following criteria to be eligible for remote work: - Successfully completed the 90-day probationary period - Role has been assessed as suitable for remote work by their manager - No active performance improvement plans (PIPs) - Manager approval obtained in writing 4.2 Hybrid Work Schedule Eligible employees may work remotely up to 3 days per week under the hybrid model. The remaining 2 days must be spent in the office unless otherwise agreed. 4.3 Fully Remote Work Fully remote work (5 days per week from home) is subject to: - Department head approval - Demonstrated 6+ months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours.

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [2]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**employee_handbook.txt** — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m [3]

months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum download speed of 50 Mbps is required - Employees must have a dedicated workspace free from distractions - Company-provided laptop must be used for all work activities - Personal home office stipend: $500 USD per year (reimbursed via expense portal) 4.6 In-Office Requirements Even while on a remote schedule, employees must attend the office for: - All-hands meetings and town halls - Quarterly performance reviews - Team-building events designated as mandatory - Client meetings requiring physical presence ============================================================= SECTION 5: COMPENSATION AND BENEFITS ============================================================= 5.1 Salary Review Salary reviews are conducted annually in March. Merit increases are based on performance ratings and company financial performance. 5.2 Performance Bonus Eligible employees may receive an annual performance bonus of up to 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense.

---

**security_policy.txt** — 4.3 Internet Use
The following are prohibited on company networks and devices:
- [4]

- All remote access (VPN, remote desktop) - Access to cloud services (Microsoft 365, AWS, Google Workspace) - Access to HR and financial systems - Administrative accounts Approved MFA methods: Authenticator apps (Microsoft Authenticator, Google Authenticator), hardware tokens. SMS-based MFA is deprecated and will be phased out by Q3 2025. 2.4 Account Lockout Policy Accounts are locked after 5 consecutive failed login attempts. Lockout duration: 30 minutes (self-unlock) or contact IT support for immediate unlock. ============================================================= SECTION 3: DATA CLASSIFICATION AND HANDLING ============================================================= 3.1 Data Classification Levels - Public: Information approved for public release - Internal: General business information for employee use - Confidential: Sensitive business data requiring access controls - Restricted: Highly sensitive data (PII, financial records, IP) 3.2 Handling Rules - Restricted data must be encrypted at rest and in transit - Confidential data must not be stored on personal devices - All data shared externally must be approved by a department head - USB drives are prohibited for data transfer of Confidential or Restricted data ============================================================= SECTION 4: ACCEPTABLE USE POLICY ============================================================= 4.1 Company Equipment Company-provided equipment must be used primarily for business purposes. Limited personal use is permitted provided it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice.

---

**security_policy.txt** — 2.4 Account Lockout Policy
Accounts are locked after 5 consecutive failed login  [5]

INFORMATION SECURITY POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IS-001 | Version 2.1 | Last Updated: March 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: PURPOSE AND SCOPE ============================================================= This policy establishes the information security requirements for all Acme Corp employees, contractors, and third-party users who access company systems or data. Non-compliance may result in disciplinary action up to and including termination. ============================================================= SECTION 2: PASSWORD REQUIREMENTS ============================================================= 2.1 Password Complexity All user account passwords must meet the following requirements: - Minimum length: 12 characters - Must include at least one uppercase letter (A-Z) - Must include at least one lowercase letter (a-z) - Must include at least one number (0-9) - Must include at least one special character (!@#$%^&*) - Must not contain the user's name, email address, or username - Must not be a previously used password (last 12 passwords are blocked) 2.2 Password Expiry Passwords must be changed every 90 days. Users will receive a reminder 14 days before expiry. Failure to update passwords will result in account lockout. 2.3 Multi-Factor Authentication (MFA) MFA is mandatory for: - All remote access (VPN, remote desktop) - Access to cloud services (Microsoft 365, AWS, Google Workspace) - Access to HR and financial systems - Administrative accounts Approved MFA methods: Authenticator apps (Microsoft Authenticator, Google Authenticator), hardware tokens. SMS-based MFA is deprecated and will be phased out by Q3 2025.

**Grounded:** True

**Relevance Score:** 0.8019

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Relevance: Very High - 0.8019)
- **[2] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: Very High - 0.7962)
- **[3] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: High - 0.6706)
- **[4] security_policy.txt** — Section: 4.3 Internet Use
The following are prohibited on company networks and devices:
- (Relevance: High - 0.6445)
- **[5] security_policy.txt** — Section: 2.4 Account Lockout Policy
Accounts are locked after 5 consecutive failed login  (Relevance: High - 0.5905)

### Supporting Passages:

#### [1] Excerpt:
> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ===========================================...

#### [2] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [3] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

#### [4] Excerpt:
> - All remote access (VPN, remote desktop) - Access to cloud services (Microsoft 365, AWS, Google Workspace) - Access to HR and financial systems - Administrative accounts Approved MFA methods: Authenticator apps (Microsoft Authenticator, Google Authenticator), hardware tokens. SMS-based MFA is deprecated and will be phased out by Q3 2025. 2.4 Account Lockout Policy Accounts are locked after 5 cons...

#### [5] Excerpt:
> INFORMATION SECURITY POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IS-001 | Version 2.1 | Last Updated: March 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: PURPOSE AND SCOPE ============================================================= This policy establishes the information security re...

---

## Question 4: What are the password requirements?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**security_policy.txt** — 2.4 Account Lockout Policy
Accounts are locked after 5 consecutive failed login  [1]

INFORMATION SECURITY POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IS-001 | Version 2.1 | Last Updated: March 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: PURPOSE AND SCOPE ============================================================= This policy establishes the information security requirements for all Acme Corp employees, contractors, and third-party users who access company systems or data. Non-compliance may result in disciplinary action up to and including termination. ============================================================= SECTION 2: PASSWORD REQUIREMENTS ============================================================= 2.1 Password Complexity All user account passwords must meet the following requirements: - Minimum length: 12 characters - Must include at least one uppercase letter (A-Z) - Must include at least one lowercase letter (a-z) - Must include at least one number (0-9) - Must include at least one special character (!@#$%^&*) - Must not contain the user's name, email address, or username - Must not be a previously used password (last 12 passwords are blocked) 2.2 Password Expiry Passwords must be changed every 90 days. Users will receive a reminder 14 days before expiry. Failure to update passwords will result in account lockout. 2.3 Multi-Factor Authentication (MFA) MFA is mandatory for: - All remote access (VPN, remote desktop) - Access to cloud services (Microsoft 365, AWS, Google Workspace) - Access to HR and financial systems - Administrative accounts Approved MFA methods: Authenticator apps (Microsoft Authenticator, Google Authenticator), hardware tokens. SMS-based MFA is deprecated and will be phased out by Q3 2025.

---

**it_support_guide.txt** — 4.2 Email Issues
1. Restart Outlook or clear the Outlook cache
2. Check account  [2]

client (Cisco AnyConnect) - Password Manager (1Password) Role-specific software is installed upon request to IT. ============================================================= SECTION 2: IT SUPPORT CHANNELS ============================================================= 2.1 Self-Service Portal Access the IT Self-Service Portal at: it-support.acmecorp.example.com Available 24/7 for: - Password resets - Software installation requests - Account unlock requests - Common troubleshooting guides 2.2 Helpdesk Contact - Email: itsupport@acmecorp.example.com (response within 4 business hours) - Phone: Extension 5500 (available 8:00 AM – 6:00 PM local time) - Slack: #it-support channel (monitored during business hours) - Walk-in: IT Office, Floor 3, Main Building (9:00 AM – 5:00 PM) 2.3 After-Hours Support For critical system outages outside business hours: - Emergency hotline: +1-800-555-0200 - Email: it-emergency@acmecorp.example.com ============================================================= SECTION 3: SUPPORT PRIORITY LEVELS ============================================================= P1 - Critical (Response: 1 hour, Resolution: 4 hours) Examples: Complete system outage, data breach, production failure P2 - High (Response: 2 hours, Resolution: 8 hours) Examples: Email not working, VPN down, cannot access critical application P3 - Medium (Response: 4 hours, Resolution: 1 business day) Examples: Software not working, printer issues, minor access problems P4 - Low (Response: 1 business day, Resolution: 3 business days) Examples: New software requests, hardware upgrades, enhancement requests ============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after these steps

---

**employee_handbook.txt** — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m [3]

months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum download speed of 50 Mbps is required - Employees must have a dedicated workspace free from distractions - Company-provided laptop must be used for all work activities - Personal home office stipend: $500 USD per year (reimbursed via expense portal) 4.6 In-Office Requirements Even while on a remote schedule, employees must attend the office for: - All-hands meetings and town halls - Quarterly performance reviews - Team-building events designated as mandatory - Client meetings requiring physical presence ============================================================= SECTION 5: COMPENSATION AND BENEFITS ============================================================= 5.1 Salary Review Salary reviews are conducted annually in March. Merit increases are based on performance ratings and company financial performance. 5.2 Performance Bonus Eligible employees may receive an annual performance bonus of up to 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense.

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [4]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**it_support_guide.txt** — 5.2 Lost or Stolen Devices
Report immediately to:
- IT Security: security@acmeco [5]

============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after these steps 4.2 Email Issues 1. Restart Outlook or clear the Outlook cache 2. Check account settings: SMTP/IMAP settings in IT Portal 3. Verify Microsoft 365 service status at status.microsoft.com 4. Contact IT if unable to send or receive email after 15 minutes 4.3 Password Reset Self-service password reset available at: password-reset.acmecorp.example.com Requires MFA verification and answers to security questions. ============================================================= SECTION 5: DEVICE MANAGEMENT ============================================================= 5.1 Device Refresh Cycle Company laptops are replaced every 3 years or when no longer fit for purpose. Refresh requests must be submitted through the IT Portal. 5.2 Lost or Stolen Devices Report immediately to: - IT Security: security@acmecorp.example.com - Your direct manager - Local law enforcement if theft is suspected Reporting deadline: Within 4 hours of discovery. The device will be remotely wiped upon receipt of the lost/stolen report. ============================================================= END OF DOCUMENT =============================================================

**Grounded:** True

**Relevance Score:** 0.7675

### Sources Cited:

- **[1] security_policy.txt** — Section: 2.4 Account Lockout Policy
Accounts are locked after 5 consecutive failed login  (Relevance: Very High - 0.7675)
- **[2] it_support_guide.txt** — Section: 4.2 Email Issues
1. Restart Outlook or clear the Outlook cache
2. Check account  (Relevance: High - 0.5816)
- **[3] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: High - 0.5783)
- **[4] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: High - 0.5756)
- **[5] it_support_guide.txt** — Section: 5.2 Lost or Stolen Devices
Report immediately to:
- IT Security: security@acmeco (Relevance: High - 0.5556)

### Supporting Passages:

#### [1] Excerpt:
> INFORMATION SECURITY POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IS-001 | Version 2.1 | Last Updated: March 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: PURPOSE AND SCOPE ============================================================= This policy establishes the information security re...

#### [2] Excerpt:
> client (Cisco AnyConnect) - Password Manager (1Password) Role-specific software is installed upon request to IT. ============================================================= SECTION 2: IT SUPPORT CHANNELS ============================================================= 2.1 Self-Service Portal Access the IT Self-Service Portal at: it-support.acmecorp.example.com Available 24/7 for: - Password resets...

#### [3] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

#### [4] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [5] Excerpt:
> ============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after thes...

---

## Question 5: What are the main requirements for working remotely?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu [1]

required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ============================================================= 4.1 Eligibility Requirements Employees must meet ALL of the following criteria to be eligible for remote work: - Successfully completed the 90-day probationary period - Role has been assessed as suitable for remote work by their manager - No active performance improvement plans (PIPs) - Manager approval obtained in writing 4.2 Hybrid Work Schedule Eligible employees may work remotely up to 3 days per week under the hybrid model. The remaining 2 days must be spent in the office unless otherwise agreed. 4.3 Fully Remote Work Fully remote work (5 days per week from home) is subject to: - Department head approval - Demonstrated 6+ months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours.

---

**it_support_guide.txt** — 4.2 Email Issues
1. Restart Outlook or clear the Outlook cache
2. Check account  [2]

client (Cisco AnyConnect) - Password Manager (1Password) Role-specific software is installed upon request to IT. ============================================================= SECTION 2: IT SUPPORT CHANNELS ============================================================= 2.1 Self-Service Portal Access the IT Self-Service Portal at: it-support.acmecorp.example.com Available 24/7 for: - Password resets - Software installation requests - Account unlock requests - Common troubleshooting guides 2.2 Helpdesk Contact - Email: itsupport@acmecorp.example.com (response within 4 business hours) - Phone: Extension 5500 (available 8:00 AM – 6:00 PM local time) - Slack: #it-support channel (monitored during business hours) - Walk-in: IT Office, Floor 3, Main Building (9:00 AM – 5:00 PM) 2.3 After-Hours Support For critical system outages outside business hours: - Emergency hotline: +1-800-555-0200 - Email: it-emergency@acmecorp.example.com ============================================================= SECTION 3: SUPPORT PRIORITY LEVELS ============================================================= P1 - Critical (Response: 1 hour, Resolution: 4 hours) Examples: Complete system outage, data breach, production failure P2 - High (Response: 2 hours, Resolution: 8 hours) Examples: Email not working, VPN down, cannot access critical application P3 - Medium (Response: 4 hours, Resolution: 1 business day) Examples: Software not working, printer issues, minor access problems P4 - Low (Response: 1 business day, Resolution: 3 business days) Examples: New software requests, hardware upgrades, enhancement requests ============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after these steps

---

**employee_handbook.txt** — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m [3]

months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum download speed of 50 Mbps is required - Employees must have a dedicated workspace free from distractions - Company-provided laptop must be used for all work activities - Personal home office stipend: $500 USD per year (reimbursed via expense portal) 4.6 In-Office Requirements Even while on a remote schedule, employees must attend the office for: - All-hands meetings and town halls - Quarterly performance reviews - Team-building events designated as mandatory - Client meetings requiring physical presence ============================================================= SECTION 5: COMPENSATION AND BENEFITS ============================================================= 5.1 Salary Review Salary reviews are conducted annually in March. Merit increases are based on performance ratings and company financial performance. 5.2 Performance Bonus Eligible employees may receive an annual performance bonus of up to 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense.

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [4]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**it_support_guide.txt** — 5.2 Lost or Stolen Devices
Report immediately to:
- IT Security: security@acmeco [5]

============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after these steps 4.2 Email Issues 1. Restart Outlook or clear the Outlook cache 2. Check account settings: SMTP/IMAP settings in IT Portal 3. Verify Microsoft 365 service status at status.microsoft.com 4. Contact IT if unable to send or receive email after 15 minutes 4.3 Password Reset Self-service password reset available at: password-reset.acmecorp.example.com Requires MFA verification and answers to security questions. ============================================================= SECTION 5: DEVICE MANAGEMENT ============================================================= 5.1 Device Refresh Cycle Company laptops are replaced every 3 years or when no longer fit for purpose. Refresh requests must be submitted through the IT Portal. 5.2 Lost or Stolen Devices Report immediately to: - IT Security: security@acmecorp.example.com - Your direct manager - Local law enforcement if theft is suspected Reporting deadline: Within 4 hours of discovery. The device will be remotely wiped upon receipt of the lost/stolen report. ============================================================= END OF DOCUMENT =============================================================

**Grounded:** True

**Relevance Score:** 0.7616

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Relevance: Very High - 0.7616)
- **[2] it_support_guide.txt** — Section: 4.2 Email Issues
1. Restart Outlook or clear the Outlook cache
2. Check account  (Relevance: High - 0.7395)
- **[3] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: High - 0.688)
- **[4] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: High - 0.6848)
- **[5] it_support_guide.txt** — Section: 5.2 Lost or Stolen Devices
Report immediately to:
- IT Security: security@acmeco (Relevance: High - 0.6548)

### Supporting Passages:

#### [1] Excerpt:
> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ===========================================...

#### [2] Excerpt:
> client (Cisco AnyConnect) - Password Manager (1Password) Role-specific software is installed upon request to IT. ============================================================= SECTION 2: IT SUPPORT CHANNELS ============================================================= 2.1 Self-Service Portal Access the IT Self-Service Portal at: it-support.acmecorp.example.com Available 24/7 for: - Password resets...

#### [3] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

#### [4] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [5] Excerpt:
> ============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after thes...

---

## Question 6: How do the leave and remote work policies relate to each other?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c [1]

EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across multiple offices globally with a remote-first culture. This handbook outlines the policies, procedures, and guidelines that govern employment at Acme Corp. All employees are expected to read and comply with the policies described herein. Questions should be directed to Human Resources at hr@acmecorp.example.com. ============================================================= SECTION 2: EMPLOYMENT POLICIES ============================================================= 2.1 Equal Opportunity Employment Acme Corp is an equal opportunity employer. We do not discriminate on the basis of race, color, religion, gender, national origin, age, disability, or any other protected characteristic. 2.2 Probationary Period All new employees serve a 90-day probationary period. During this period: - Performance is closely monitored - Benefits eligibility may be limited (see Section 5) - Remote work is not permitted (see Section 4) - Employment may be terminated without notice 2.3 Employment Classifications - Full-time: 40 hours per week, eligible for all benefits - Part-time: Less than 30 hours per week, limited benefits - Contract: Project-based, no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis.

---

**employee_handbook.txt** — 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu [2]

required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ============================================================= 4.1 Eligibility Requirements Employees must meet ALL of the following criteria to be eligible for remote work: - Successfully completed the 90-day probationary period - Role has been assessed as suitable for remote work by their manager - No active performance improvement plans (PIPs) - Manager approval obtained in writing 4.2 Hybrid Work Schedule Eligible employees may work remotely up to 3 days per week under the hybrid model. The remaining 2 days must be spent in the office unless otherwise agreed. 4.3 Fully Remote Work Fully remote work (5 days per week from home) is subject to: - Department head approval - Demonstrated 6+ months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours.

---

**employee_handbook.txt** — 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t [3]

no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis. 3.2 Leave Carry-Forward Unused annual leave may be carried forward to the next calendar year, subject to a maximum carry-forward of 5 days. Leave exceeding this limit will be forfeited. 3.3 Leave Request Procedure - All leave requests must be submitted at least 14 calendar days (2 weeks) in advance - Requests must be submitted through the HR Portal at hr-portal.acmecorp.example.com - Manager approval is required before leave is confirmed - Emergency leave may be granted with shorter notice subject to manager discretion 3.4 Public Holidays Acme Corp observes all nationally recognized public holidays. These days are in addition to the annual leave entitlement and are not deducted from the leave balance. 3.5 Sick Leave Employees are entitled to 10 days of paid sick leave per year. Sick leave does not carry forward. Medical certificates are required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY =============================================================

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [4]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**employee_handbook.txt** — 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m [5]

months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum download speed of 50 Mbps is required - Employees must have a dedicated workspace free from distractions - Company-provided laptop must be used for all work activities - Personal home office stipend: $500 USD per year (reimbursed via expense portal) 4.6 In-Office Requirements Even while on a remote schedule, employees must attend the office for: - All-hands meetings and town halls - Quarterly performance reviews - Team-building events designated as mandatory - Client meetings requiring physical presence ============================================================= SECTION 5: COMPENSATION AND BENEFITS ============================================================= 5.1 Salary Review Salary reviews are conducted annually in March. Merit increases are based on performance ratings and company financial performance. 5.2 Performance Bonus Eligible employees may receive an annual performance bonus of up to 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense.

**Grounded:** True

**Relevance Score:** 0.8307

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Relevance: Very High - 0.8307)
- **[2] employee_handbook.txt** — Section: 4.5 Equipment and Internet Requirements
- Stable internet connection with minimu (Relevance: High - 0.6943)
- **[3] employee_handbook.txt** — Section: 4.1 Eligibility Requirements
Employees must meet ALL of the following criteria t (Relevance: High - 0.6329)
- **[4] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: Medium - 0.5319)
- **[5] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: Medium - 0.5301)

### Supporting Passages:

#### [1] Excerpt:
> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across mult...

#### [2] Excerpt:
> required for absences exceeding 3 consecutive days. 3.6 Maternity and Paternity Leave - Maternity leave: 26 weeks (first 16 weeks fully paid, remaining 10 weeks at 50% pay) - Paternity leave: 4 weeks fully paid - Adoption leave: Same as maternity leave entitlement ============================================================= SECTION 4: REMOTE WORK POLICY ===========================================...

#### [3] Excerpt:
> no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-...

#### [4] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [5] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

---

## Question 7: What are the main employee responsibilities described in the policies?

**Answer:**

*Note: LLM API key is not configured. Please configure the required environment variable to use Research Agent answer synthesis. Showing local evidence-only fallback passages.*


---

**employee_handbook.txt** — 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c [1]

EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across multiple offices globally with a remote-first culture. This handbook outlines the policies, procedures, and guidelines that govern employment at Acme Corp. All employees are expected to read and comply with the policies described herein. Questions should be directed to Human Resources at hr@acmecorp.example.com. ============================================================= SECTION 2: EMPLOYMENT POLICIES ============================================================= 2.1 Equal Opportunity Employment Acme Corp is an equal opportunity employer. We do not discriminate on the basis of race, color, religion, gender, national origin, age, disability, or any other protected characteristic. 2.2 Probationary Period All new employees serve a 90-day probationary period. During this period: - Performance is closely monitored - Benefits eligibility may be limited (see Section 5) - Remote work is not permitted (see Section 4) - Employment may be terminated without notice 2.3 Employment Classifications - Full-time: 40 hours per week, eligible for all benefits - Part-time: Less than 30 hours per week, limited benefits - Contract: Project-based, no employee benefits ============================================================= SECTION 3: ANNUAL LEAVE AND TIME OFF ============================================================= 3.1 Annual Leave Entitlement Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at a rate of 1.67 days per month of employment. Part-time employees receive leave on a pro-rata basis.

---

**security_policy.txt** — 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from [2]

it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are prohibited on company networks and devices: - Downloading or distributing copyrighted material without authorization - Accessing adult content, gambling, or illegal websites - Running personal businesses or side projects - Cryptocurrency mining ============================================================= SECTION 5: INCIDENT REPORTING ============================================================= 5.1 What to Report Employees must report the following immediately: - Lost or stolen company devices - Suspected phishing emails or social engineering attempts - Unauthorized access to systems or data - Data breaches or accidental data disclosure 5.2 How to Report - Email: security@acmecorp.example.com (monitored 24/7) - Phone: IT Security Hotline +1-800-555-0100 - Internal portal: security.acmecorp.example.com/report 5.3 Reporting Timeframes - Critical incidents (data breach, active threat): Immediately, within 1 hour - High-priority (lost device, account compromise): Within 4 hours - Standard incidents: Within 24 hours ============================================================= SECTION 6: REMOTE ACCESS SECURITY ============================================================= 6.1 VPN Requirement All remote access to company systems must be through the corporate VPN. Direct access to internal systems from the public internet is prohibited. 6.2 Home Network Security Remote workers must ensure: - Home Wi-Fi router uses WPA3 or WPA2 encryption - Router firmware is kept up to date - Guest network is separate from the working network

---

**security_policy.txt** — 4.3 Internet Use
The following are prohibited on company networks and devices:
- [3]

- All remote access (VPN, remote desktop) - Access to cloud services (Microsoft 365, AWS, Google Workspace) - Access to HR and financial systems - Administrative accounts Approved MFA methods: Authenticator apps (Microsoft Authenticator, Google Authenticator), hardware tokens. SMS-based MFA is deprecated and will be phased out by Q3 2025. 2.4 Account Lockout Policy Accounts are locked after 5 consecutive failed login attempts. Lockout duration: 30 minutes (self-unlock) or contact IT support for immediate unlock. ============================================================= SECTION 3: DATA CLASSIFICATION AND HANDLING ============================================================= 3.1 Data Classification Levels - Public: Information approved for public release - Internal: General business information for employee use - Confidential: Sensitive business data requiring access controls - Restricted: Highly sensitive data (PII, financial records, IP) 3.2 Handling Rules - Restricted data must be encrypted at rest and in transit - Confidential data must not be stored on personal devices - All data shared externally must be approved by a department head - USB drives are prohibited for data transfer of Confidential or Restricted data ============================================================= SECTION 4: ACCEPTABLE USE POLICY ============================================================= 4.1 Company Equipment Company-provided equipment must be used primarily for business purposes. Limited personal use is permitted provided it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice.

---

**employee_handbook.txt** — 6.2 Anti-Harassment Policy
Acme Corp has a zero-tolerance policy for harassment  [4]

15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense. 5.4 Retirement Plan Employees are eligible for the company 401(k) plan after 3 months of employment. Acme Corp matches contributions up to 4% of base salary. ============================================================= SECTION 6: CODE OF CONDUCT ============================================================= 6.1 Professional Behavior All employees must maintain professional conduct in the workplace, including: - Treating all colleagues, clients, and partners with respect - Maintaining confidentiality of company and client information - Avoiding conflicts of interest 6.2 Anti-Harassment Policy Acme Corp has a zero-tolerance policy for harassment of any kind. All complaints must be reported to HR within 30 days of the incident. ============================================================= END OF DOCUMENT =============================================================

---

**it_support_guide.txt** — 4.2 Email Issues
1. Restart Outlook or clear the Outlook cache
2. Check account  [5]

client (Cisco AnyConnect) - Password Manager (1Password) Role-specific software is installed upon request to IT. ============================================================= SECTION 2: IT SUPPORT CHANNELS ============================================================= 2.1 Self-Service Portal Access the IT Self-Service Portal at: it-support.acmecorp.example.com Available 24/7 for: - Password resets - Software installation requests - Account unlock requests - Common troubleshooting guides 2.2 Helpdesk Contact - Email: itsupport@acmecorp.example.com (response within 4 business hours) - Phone: Extension 5500 (available 8:00 AM – 6:00 PM local time) - Slack: #it-support channel (monitored during business hours) - Walk-in: IT Office, Floor 3, Main Building (9:00 AM – 5:00 PM) 2.3 After-Hours Support For critical system outages outside business hours: - Emergency hotline: +1-800-555-0200 - Email: it-emergency@acmecorp.example.com ============================================================= SECTION 3: SUPPORT PRIORITY LEVELS ============================================================= P1 - Critical (Response: 1 hour, Resolution: 4 hours) Examples: Complete system outage, data breach, production failure P2 - High (Response: 2 hours, Resolution: 8 hours) Examples: Email not working, VPN down, cannot access critical application P3 - Medium (Response: 4 hours, Resolution: 1 business day) Examples: Software not working, printer issues, minor access problems P4 - Low (Response: 1 business day, Resolution: 3 business days) Examples: New software requests, hardware upgrades, enhancement requests ============================================================= SECTION 4: COMMON TROUBLESHOOTING ============================================================= 4.1 VPN Issues 1. Ensure you are not already connected to the VPN 2. Restart the Cisco AnyConnect client 3. Check your MFA device is connected and working 4. Verify your internet connection is active 5. Contact IT if issue persists after these steps

**Grounded:** True

**Relevance Score:** 0.8518

### Sources Cited:

- **[1] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Relevance: Very High - 0.8518)
- **[2] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: High - 0.6392)
- **[3] security_policy.txt** — Section: 4.3 Internet Use
The following are prohibited on company networks and devices:
- (Relevance: Medium - 0.5343)
- **[4] employee_handbook.txt** — Section: 6.2 Anti-Harassment Policy
Acme Corp has a zero-tolerance policy for harassment  (Relevance: Medium - 0.4927)
- **[5] it_support_guide.txt** — Section: 4.2 Email Issues
1. Restart Outlook or clear the Outlook cache
2. Check account  (Relevance: Medium - 0.4892)

### Supporting Passages:

#### [1] Excerpt:
> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across mult...

#### [2] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [3] Excerpt:
> - All remote access (VPN, remote desktop) - Access to cloud services (Microsoft 365, AWS, Google Workspace) - Access to HR and financial systems - Administrative accounts Approved MFA methods: Authenticator apps (Microsoft Authenticator, Google Authenticator), hardware tokens. SMS-based MFA is deprecated and will be phased out by Q3 2025. 2.4 Account Lockout Policy Accounts are locked after 5 cons...

#### [4] Excerpt:
> 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense. 5.4 Retirement Plan Employees are eligible for the company 401(k) plan after 3 months of...

#### [5] Excerpt:
> client (Cisco AnyConnect) - Password Manager (1Password) Role-specific software is installed upon request to IT. ============================================================= SECTION 2: IT SUPPORT CHANNELS ============================================================= 2.1 Self-Service Portal Access the IT Self-Service Portal at: it-support.acmecorp.example.com Available 24/7 for: - Password resets...

---

## Question 8: What was the company's revenue last year?

**Answer:**

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

**Grounded:** False

**Relevance Score:** 0.7884

### Sources Cited:

- **[1] expense_policy.txt** — Section: 3.1 Submission Portal
All expenses must be submitted through the Expense Portal  (Relevance: Very High - 0.7884)
- **[2] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: Very High - 0.7527)
- **[3] security_policy.txt** — Section: 2.4 Account Lockout Policy
Accounts are locked after 5 consecutive failed login  (Relevance: High - 0.6748)
- **[4] it_support_guide.txt** — Section: 2.2 Helpdesk Contact
- Email: itsupport@acmecorp.example.com (response within 4  (Relevance: High - 0.6611)
- **[5] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: High - 0.5737)

### Supporting Passages:

#### [1] Excerpt:
> EXPENSE REIMBURSEMENT POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: FIN-003 | Version 1.8 | Last Updated: February 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: OVERVIEW ============================================================= This policy governs the reimbursement of business-relat...

#### [2] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [3] Excerpt:
> INFORMATION SECURITY POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IS-001 | Version 2.1 | Last Updated: March 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: PURPOSE AND SCOPE ============================================================= This policy establishes the information security re...

#### [4] Excerpt:
> IT SUPPORT AND ONBOARDING GUIDE — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IT-002 | Version 2.0 | Last Updated: January 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: NEW EMPLOYEE IT SETUP ============================================================= 1.1 Pre-Start Setup (1 Week Before) Befor...

#### [5] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

---

## Question 9: Who is the company's CEO?

**Answer:**

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

**Grounded:** False

**Relevance Score:** 0.7204

### Sources Cited:

- **[1] expense_policy.txt** — Section: 5.2 Usage Rules
- Corporate cards must only be used for approved business expens (Relevance: High - 0.7204)
- **[2] security_policy.txt** — Section: 2.4 Account Lockout Policy
Accounts are locked after 5 consecutive failed login  (Relevance: High - 0.7025)
- **[3] it_support_guide.txt** — Section: 2.2 Helpdesk Contact
- Email: itsupport@acmecorp.example.com (response within 4  (Relevance: Medium - 0.4998)
- **[4] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Relevance: Medium - 0.4693)
- **[5] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: Medium - 0.4662)

### Supporting Passages:

#### [1] Excerpt:
> personal items - Expenses for spouses, partners, or family members (unless pre-approved) - Upgrades beyond policy limits (e.g., first class when business class is the maximum) - Expenses incurred after employee resignation or termination - Expenses without valid receipts (for amounts over $25) ============================================================= SECTION 5: CORPORATE CREDIT CARD ==========...

#### [2] Excerpt:
> INFORMATION SECURITY POLICY — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IS-001 | Version 2.1 | Last Updated: March 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: PURPOSE AND SCOPE ============================================================= This policy establishes the information security re...

#### [3] Excerpt:
> IT SUPPORT AND ONBOARDING GUIDE — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IT-002 | Version 2.0 | Last Updated: January 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: NEW EMPLOYEE IT SETUP ============================================================= 1.1 Pre-Start Setup (1 Week Before) Befor...

#### [4] Excerpt:
> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across mult...

#### [5] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

---

## Question 10: What is the company's stock price today?

**Answer:**

I couldn't find enough information in the provided knowledge-base sources to answer this question reliably.

**Sources consulted:** None sufficiently relevant.

Please check if the relevant document has been added to the knowledge base, or rephrase your question.

**Grounded:** False

**Relevance Score:** 0.7193

### Sources Cited:

- **[1] security_policy.txt** — Section: 6.3 Physical Security
Remote workers must:
- Lock screen when stepping away from (Relevance: High - 0.7193)
- **[2] it_support_guide.txt** — Section: 2.2 Helpdesk Contact
- Email: itsupport@acmecorp.example.com (response within 4  (Relevance: Medium - 0.4576)
- **[3] employee_handbook.txt** — Section: 6.2 Anti-Harassment Policy
Acme Corp has a zero-tolerance policy for harassment  (Relevance: Medium - 0.4304)
- **[4] employee_handbook.txt** — Section: 3.2 Leave Carry-Forward
Unused annual leave may be carried forward to the next c (Relevance: Medium - 0.4141)
- **[5] employee_handbook.txt** — Section: 5.4 Retirement Plan
Employees are eligible for the company 401(k) plan after 3 m (Relevance: Medium - 0.4114)

### Supporting Passages:

#### [1] Excerpt:
> it does not: - Involve illegal activities - Compromise system security - Consume excessive network resources - Interfere with work responsibilities 4.2 Software Installation Only IT-approved software may be installed on company devices. Software installation requests must be submitted through the IT Portal. Unauthorized software may be removed without notice. 4.3 Internet Use The following are pro...

#### [2] Excerpt:
> IT SUPPORT AND ONBOARDING GUIDE — ACME CORP (SAMPLE / FICTIONAL) Policy Reference: IT-002 | Version 2.0 | Last Updated: January 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: NEW EMPLOYEE IT SETUP ============================================================= 1.1 Pre-Start Setup (1 Week Before) Befor...

#### [3] Excerpt:
> 15% of base salary, awarded in April based on the prior year's performance. 5.3 Health Insurance Acme Corp provides comprehensive health insurance for all full-time employees. Coverage begins on the first day of the month following the start date. Dependents may be added to the plan at the employee's expense. 5.4 Retirement Plan Employees are eligible for the company 401(k) plan after 3 months of...

#### [4] Excerpt:
> EMPLOYEE HANDBOOK — ACME CORP (SAMPLE / FICTIONAL) Version 3.2 | Effective Date: January 1, 2025 This is a fictional sample document for demonstration purposes only. ============================================================= SECTION 1: COMPANY OVERVIEW ============================================================= Acme Corp is a technology services company founded in 2005. We operate across mult...

#### [5] Excerpt:
> months of successful hybrid work - Role classification as remote-eligible by HR - Annual review and reconfirmation 4.4 Core Hours Requirement All remote workers must be available during core hours: 10:00 AM to 3:00 PM local time. Outside core hours, employees are expected to respond to messages within 2 hours. 4.5 Equipment and Internet Requirements - Stable internet connection with minimum downlo...

---

