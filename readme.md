# JobScanGPT [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://JobScanGPT.streamlit.app/) [![](https://img.shields.io/github/license/yuting1214/JobScanGPT)](https://github.com/yuting1214/JobScanGPT/blob/main/LICENSE)

JobScanGPT is an LLM-based application designed to help users streamline the process of analyzing job descriptions.
By scanning the provided job description, the app extracts key information, saving time and enhancing efficiency. :hourglass_flowing_sand:
![](https://github.com/yuting1214/JobScanGPT/blob/main/material/JobScan_Demo.gif)
## :arrow_down: Installation
### Packages
```
pip install openai python-dotenv streamlit
```
or 
```
pip install -r requirements.txt
```
### API Key

Create a file named **.env** under the folder of **API_key** .

Add the following line in that file:
```
OPENAI_API_KEY=<Your API key>
```

## :rocket: Quickstart
After clone, run
```
streamlit run llm_app.py
```

## :robot: ChatGPT version(valid for GPT-3.5, GPT4)
Start a **New chat console**, then copy and paste the following instruction prompt and submit it first.
```
You will be given a job description.

Your task is to extract or classify certain key information from the description.
If the information isn't explicitly mentioned in the job description, don't make any assumptions - simply respond with 'Not mentioned'.
If there are [options] provided for a certain task, only include those [options] in the exact word.

Company's name: Extract Company's name with exact words or [not mentioned] if it could not be extracted.

Industry: Identify the industry that the company is in or [not mentioned] if it is not specified in the description.

Citizenship Requirement: Identify whether the job requires the applicant to be a [Permanent Resident only] or if this requirement is [not mentioned].

Visa Sponsor Policy: Identify whether the company [Will provide] visa sponsorship or [Will not provide] visa sponsorship or if this policy is [not mentioned].

Job type:  Classify one of [Full time, Intern, Contractor]

Years of Experience: Extract required YoE in years from the description.

Years of Experience level: Classify whether the job requires a [New grad] with under one year of experience,
a [Mid-level] professional with 1 to 3 years of experience,
a [Senior] professional with more than 3 years of experience, or if this requirement is [not mentioned].
Use the information extracted from the `Years of Experience` to make this decision.

Top Three Data science relevant Skills: Identify the top three technological skills required for the job.

Domain Knowledge Required: Identify any specific domain/Industry knowledge required for the job.

Minimum Education: Choose only one as the minimum requirement among [Phd only], [Master], [Bachelor], or [not mentioned]. If multiple degrees are mentioned, select the lowest qualification as the minimum requirement.

Return JSON format with keys = [Company, Industry, Citizenship, Visa_policy, JobType, YoE_year, YoE_level, DS_skills, Domain_Knowledge, Min_Education]
Values in the returned JSON must only be either string or a list of strings if multiple elements are required.

Don't provide extra explanations. Don't give default output.

Don't reply until given input. Don't provide extra explanations. Don't give default output.
```
After receiving the response from ChatGPT, paste the job description and submit it, you will have the intended result.

> :bulb: Note the instruction prompt in this example is currently for data-relevant roles (data analyst, data scientist, data engineer); feel free to modify it to tailor your job search.

## :notebook_with_decorative_cover: Notebook version

See more in [Notebook demo](https://github.com/yuting1214/JobScanGPT/blob/main/Notebook_demo.ipynb)

## :star2: Features
- **Scan and Extract**: Identify key information in job descriptions like citizenship rules, visa policies, and experience required, all with a quick scan.
- **Cost-Aware**: See the price for a single use right when you submit the job, tailored to the LLM you pick.
- **Lightweight Database**: All the input text and output JSON will be automatically saved in the **data** folder, ready for future use or fine-tuning.
- **Intelligent and robust system**: All the sensitive input will be took care, and the input irrevalant to job descriptions will be detected in advance to prevent further processing.

## :warning: Note
* The app currently supports English language only.
* Due to network latency, it will generally take around 5 second to see the output.
* Years of Experience Level is categorized into four groups:
  * [New grad]: Under one year of experience.
  * [Mid-level]: Professional with 1 to 3 years of experience.
  * [Senior]: Professional with more than 3 years of experience.
  * [not mentioned]: If this requirement is not specified in the job description.
* Different roles have slightly different ouput:
  * [Data relevant]: {DS_skills:, }
  * [Software Engineer]: {Languages:, SE_skills:}
  * [General]: The general positions without the above extra informaiton.
* It's common for the Company's name to be omitted, especially when information is not provided in the job descriptions.
* Collected text data are organized with timestamp extensions for easy identification and sequencing.
* The collected JSON outputs are stored incrementally, preserving their order.

## :books: Reference

- **Pricing**: [OpenAI Pricing Details](https://platform.openai.com/docs/models/overview)
- **How can I access GPT-4?**: [Accessing GPT-4 Information](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4)
- **For API encryption**: [Password Hashing with Bcrypt](https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/)

## :scroll: License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Designed with :heart: by [Mark Chen](https://github.com/yuting1214)
