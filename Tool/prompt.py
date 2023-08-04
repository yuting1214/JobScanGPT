"""
This module contains prompts for extracting specific information from various job descriptions.

The prompts are designed to guide the extraction of key information such as company name, industry, 
citizenship requirement, visa sponsor policy, job type, years of experience, relevant skills, domain 
knowledge required, and minimum education. The information extracted is to be returned in a specific 
JSON format.

The prompts are divided into three categories:
- Data Science Relevant (ds_prompt): Specific to data science positions, includes extraction of top three data science relevant skills.
- Software Engineer (se_prompt): Specific to software engineering positions, includes extraction of required programming languages.
- General Positions (general_prompt): Applicable to general positions without specific technical skill extraction.

The instructions in the prompts specify the exact format and options to be returned and emphasize not making assumptions or adding extra information.
"""

# Prompt for Data science relevant
ds_prompt = f"""
You will be provided with job description queries. \
The job description query will be delimited with #### characters.\

First classify if the input is an actual job description. \
If it is not a job description, return "The input is not a job description" immediately and do not conduct the following tasks. \

Your task is to extract or classify certain key information from the description. \
If the information isn't explicitly mentioned in the job description, don't make any assumptions - simply respond with 'Not mentioned'. \
If there are [options] provided for a certain task, only return those [options] with the exact word. Don't add extra information for [options]. \

Company's name: Extract Company's name with exact words or [not mentioned] if it could not be extracted.\

Industry: Identify the industry that the company is in or [not mentioned] if it is not specified in the description. \

Citizenship Requirement: Identify whether the job requires the applicant to be a [Permanent Resident only] or if this requirement is [not mentioned]. \

Visa Sponsor Policy: Identify whether the company [Will provide], [Will not provide] visa sponsorship or if this policy is [not mentioned]. \

Job type:  Classify one of [Full time, Intern, Contractor]. If the description contains words like (Duration, Pay Rate, Per hour), classify it as [Contractor]. \

Years of Experience: Extract required YoE in years from the description. \

Years of Experience level: Classify whether the job requires a [New grad] with under one year of experience, \
a [Mid-level] professional with 1 to 3 years of experience,  \
a [Senior] professional with more than 3 years of experience, or if this requirement is [not mentioned]. \
Use the information extracted from the `Years of Experience` to make this decision. \

Top Three Data science relevant Skills: Identify the top three technological skills required for the job. \

Domain Knowledge Required: Identify any specific domain/Industry knowledge required for the job. \

Minimum Education: Choose only one as the minimum requirement among [Phd only], [Master], [Bachelor], or [not mentioned]. If multiple degrees are mentioned, select the lowest qualification as the minimum requirement. \

Return JSON format with keys = [Company, Industry, Citizenship, Visa_policy, JobType, YoE_year, YoE_level, DS_skills, Domain_Knowledge, Min_Education] \
Values in the returned JSON must only be either string or a list of strings if multiple elements are required. \

Don't provide extra explanations. Don't give default output. 
"""
# Prompt for Software Engineer
se_prompt = f"""
You will be provided with job description queries. \
The job description query will be delimited with #### characters.\

First classify if the input is an actual job description. \
If it is not a job description, return "The input is not a job description" immediately and do not conduct the following tasks. \

Your task is to extract or classify certain key information from the description. \
If the information isn't explicitly mentioned in the job description, don't make any assumptions - simply respond with 'Not mentioned'. \
If there are [options] provided for a certain task, only return those [options] with the exact word. Don't add extra information for [options]. \

Company's name: Extract Company's name with exact words or [not mentioned] if it could not be extracted.\

Industry: Identify the industry that the company is in or [not mentioned] if it is not specified in the description. \

Citizenship Requirement: Identify whether the job requires the applicant to be a [Permanent Resident only] or if this requirement is [not mentioned]. \

Visa Sponsor Policy: Identify whether the company [Will provide], [Will not provide] visa sponsorship or if this policy is [not mentioned]. \

Job type:  Classify one of [Full time, Intern, Contractor]. If the description contains words like (Duration, Pay Rate, Per hour), classify it as [Contractor]. \

Years of Experience: Extract required YoE in years from the description. \

Years of Experience level: Classify whether the job requires a [New grad] with under one year of experience, \
a [Mid-level] professional with 1 to 3 years of experience,  \
a [Senior] professional with more than 3 years of experience, or if this requirement is [not mentioned]. \
Use the information extracted from the `Years of Experience` to make this decision. \

Required Programming Languages: List all the programming languages that are essential for the software engineering position at the company. \

Top Three Software Engineering Relevant Skills: Identify the top three technological skills required for the software engineering job. \

Domain Knowledge Required: Identify any specific domain/Industry knowledge required for the job. \

Minimum Education: Choose only one as the minimum requirement among [Phd only], [Master], [Bachelor], or [not mentioned]. If multiple degrees are mentioned, select the lowest qualification as the minimum requirement. \

Return JSON format with keys = [Company, Industry, Citizenship, Visa_policy, JobType, YoE_year, YoE_level, Languages, SE_skills, Domain_Knowledge, Min_Education] \
Values in the returned JSON must only be either string or a list of strings if multiple elements are required. \

Don't provide extra explanations. Don't give default output. 
"""

# Prompt for General positions
general_prompt = f"""
You will be provided with job description queries. \
The job description query will be delimited with #### characters.\

First classify if the input is an actual job description. \
If it is not a job description, return "The input is not a job description" immediately and do not conduct the following tasks. \

Your task is to extract or classify certain key information from the description. \
If the information isn't explicitly mentioned in the job description, don't make any assumptions - simply respond with 'Not mentioned'. \
If there are [options] provided for a certain task, only return those [options] with the exact word. Don't add extra information for [options]. \

Company's name: Extract Company's name with exact words or [not mentioned] if it could not be extracted.\

Industry: Identify the industry that the company is in or [not mentioned] if it is not specified in the description. \

Citizenship Requirement: Identify whether the job requires the applicant to be a [Permanent Resident only] or if this requirement is [not mentioned]. \

Visa Sponsor Policy: Identify whether the company [Will provide], [Will not provide] visa sponsorship or if this policy is [not mentioned]. \

Job type:  Classify one of [Full time, Intern, Contractor]. If the description contains words like (Duration, Pay Rate, Per hour), classify it as [Contractor]. \

Years of Experience: Extract required YoE in years from the description. \

Years of Experience level: Classify whether the job requires a [New grad] with under one year of experience, \
a [Mid-level] professional with 1 to 3 years of experience,  \
a [Senior] professional with more than 3 years of experience, or if this requirement is [not mentioned]. \
Use the information extracted from the `Years of Experience` to make this decision. \

Domain Knowledge Required: Identify any specific domain/Industry knowledge required for the job. \

Minimum Education: Choose only one as the minimum requirement among [Phd only], [Master], [Bachelor], or [not mentioned]. If multiple degrees are mentioned, select the lowest qualification as the minimum requirement. \

Return JSON format with keys = [Company, Industry, Citizenship, Visa_policy, JobType, YoE_year, YoE_level, Domain_Knowledge, Min_Education] \
Values in the returned JSON must only be either string or a list of strings if multiple elements are required. \

Don't provide extra explanations. Don't give default output. 
"""
