# def cover_letter_prompt(job_description: str, resume: str) -> str:
    
#     """Generate a cover letter prompt based on job description and resume"""
    
#     return f"""
#     Create a professional cover letter for the following job position using my resume. Follow this template exactly:

#     Jithin Raj Reghuvaran
#     Recent Master 2 Graduate in Data Science from France
#     Paris, France
#     (+33) 745293669 | [jithinrajr98@gmail.com](mailto:jithinrajr98@gmail.com)

#     Subject: Application for the position of [JOB TITLE]

#     Dear Hiring Manager,

#     I'm writing to express my strong interest in the [JOB TITLE] position at [COMPANY NAME]. I am recent Master 2 graduate in Data Science from France with [X] years of experience in [KEY SKILL AREA 1] and [KEY SKILL AREA 2]. I've successfully delivered results such as [SPECIFIC ACHIEVEMENT OR PROJECT TYPE].

#     My expertise with [RELEVANT TOOL/TECHNOLOGY 1], and [RELEVANT TOOL/TECHNOLOGY 2], aligns well with your requirements. For example, I [QUANTIFIED ACHIEVEMENT] by [SPECIFIC ACTION], resulting in [MEASURABLE OUTCOME].

#     I'm particularly drawn to [COMPANY NAME] because of [SPECIFIC COMPANY PROJECT/INITIATIVE OR VALUES]. My experience in [KEY EXPERTISE AREA] would enable me to contribute meaningfully to [SPECIFIC TEAM GOAL OR CHALLENGE].

#     I would welcome the opportunity to discuss how my background in [RELEVANT FIELD] could support your team's objectives.

#     Best regards,
#     Jithin Raj Reghuvaran

#     **Guidelines:**
#     1. Keep the letter concise and professional (150-200 words max)
#     2. Focus on quantifiable achievements from my resume that relate to the job
#     3. Match at least 3 key requirements from the job description
#     4. If the job description doesn't match my resume perfectly, write a brief but enthusiastic letter expressing genuine interest
#     5. Extract the company name and job title from the job description
#     6. Use specific examples and metrics where possible
#     7. Maintain a confident but humble tone
#     8. Highlight the Master 2 Data Science degree when relevant to the position

#     **Job Description:**
#     {job_description}

#     **My Resume:**
#     {resume}

#     Generate ONLY the cover letter text, no additional commentary.
#     """

def cover_letter_prompt(job_description: str, resume: str) -> str:
    
    """Generate a cover letter prompt based on job description and resume"""
    
    return f"""
    Create a professional cover letter  for the following job position using my resume. Follow this template exactly:
    
    Jithin Raj Reghuvaran
    Recent Master 2 Graduate in Data Science from France
    Paris, France
    (+33) 745293669 | [jithinrajr98@gmail.com](mailto:jithinrajr98@gmail.com)
    
    Dear [Hiring Manager],
    
    I hope this message finds you well. I am writing to express my interest in the [JOB TITLE] position at [COMPANY NAME]. With my background in [KEY SKILL AREA 1], [KEY SKILL AREA 2], and [KEY SKILL AREA 3], I am excited about the opportunity to contribute to your team.
    
    In my previous role at [Your Current/Previous Company], I led [TYPE OF INITIATIVES] that significantly boosted [MEASURABLE OUTCOME 1] and [MEASURABLE OUTCOME 2]. My experience in both [RELEVANT AREA 1] and [RELEVANT AREA 2], along with my proficiency in tools such as [TOOL 1] and [TOOL 2], aligns well with your job requirements.
    
    Attached are my CV and cover letter detailing my qualifications and accomplishments. Thank you for considering my application. I look forward to discussing how my skills and experiences align with the goals of [COMPANY NAME].
    
    Best regards,
    [Your Name]
    
    **Guidelines:**
    1. Keep the email body concise and professional (3 short paragraphs as shown)
    2. First paragraph: Express interest and highlight 2-3 key skill areas
    3. Second paragraph: Mention previous role/company and specific achievements with measurable outcomes
    4. Third paragraph: Reference attached documents and express interest in discussion
    5. Extract company name and job title from the job description
    6. Use specific tools, technologies, or strategies mentioned in the job description
    7. Focus on achievements that "significantly boosted" or improved metrics
    8. Maintain a warm, professional tone similar to the example
    9. Include "I hope this message finds you well" as the opening
    10. Replace [Your Name] with: Jithin Raj Reghuvaran
    
    **Job Description:**
    {job_description}
    
    **My Resume:**
    {resume}
    
    Generate ONLY the email subject and body text in the exact format shown above, no additional commentary.
    """

def profile_modifier_prompt(job_description: str, current_profile: str) -> str:
    
    """Generate a prompt to modify the profile section based on job description"""
    
    return f"""
Adapt the professional summary to match the target job description while maintaining credibility and core achievements. Follow these specific rules:

**ADAPTATION RULES:**
1. **Role Alignment**: Use the exact job title from the description or closest equivalent
2. **Skills Matching**: Prioritize skills mentioned in the job requirements
3. **Industry Language**: Use terminology and keywords from the job posting
4. **Achievement Preservation**: Keep all quantified achievements (dollar amounts, percentages, years)
5. **Experience Level**: Adjust experience level appropriately:
   - For senior roles: Emphasize leadership and strategic impact
   - For mid-level roles: Focus on hands-on expertise and project delivery  
   - For junior roles: Highlight relevant education, internships, or projects

**STRUCTURE TO MAINTAIN:**
- [ROLE TITLE] with [X]+ years of experience in [DOMAIN/TECHNOLOGY]
- Expert in [3 key technologies/skills that match job requirements].

**CONSTRAINTS:**
- Keep the same professional tone and confidence level
- Maintain 2 sentences maximum
- Preserve any specific client types (Fortune 500, etc.) and dollar figures
- Don't fabricate experience or skills not implied in the original

**Job Description:**
{job_description}

**Current Profile:**
{current_profile}

Return ONLY the modified profile summary, no additional text or explanations.
"""

def translation_prompt(text: str, target_language: str = "French", content_type: str = "cover letter") -> str:
    """Generate a prompt for translating professional content"""
    if content_type == "profile":
        instruction = "Translate the following professional profile summary to {target_language}."
        additional_context = "This is a CV/resume profile section that should maintain its professional impact and technical terminology. Don't translate specific technical terms like machine learning, deep learning or position names."
    else:
        instruction = f"Translate the following professional {content_type} to {target_language}."
        additional_context = f"This is a professional {content_type} that should maintain formal business correspondence standards. Don't translate specific technical terms  like machine learning, deep learning  or position names."
    
    return f"""
{instruction}

**Requirements:**
1. Maintain the professional tone and formal structure
2. Use appropriate business language conventions for {target_language}
3. Keep the formatting and structure intact
4. Preserve technical terms and industry jargon appropriately
5. Adapt cultural nuances appropriately (e.g., "Dear Hiring Manager" to "Madame, Monsieur" in French)
6. {additional_context}

**Text to translate:**
{text}

Provide ONLY the translated text, no additional commentary.
"""



def job_analysis_prompt(job_description: str) -> str:
    """Analyze job description to extract key information"""
    return f"""
Analyze the following job description and extract key information in the exact format specified below:

**COMPANY_NAME:** [Extract the company name - if not mentioned, write "Not specified"]

**POSITION:** [Extract the exact job title/position name]

**CANDIDATE_REQUIREMENTS:** [2 sentences maximum describing what the company is looking for in the ideal candidate - focus on experience, qualifications, and key attributes they want]

**TECHNICAL_SKILLS:** [2 sentences maximum listing the main technical skills, tools, programming languages, frameworks, or technologies required - be specific and include as many as mentioned]

**COMPANY_MISSION:** [1 sentence describing the company's mission, purpose, or what they do as a business - if not explicitly stated, infer from context]

**Instructions:**
- Extract information ONLY from the provided job description
- Use exact terminology and keywords from the job posting
- Be concise but comprehensive within the sentence limits
- If any information is completely missing from the job description, write "Not specified" for that section
- Focus on the most important and relevant details for each category
- Maintain professional language and avoid speculation beyond what's stated

**Job Description:**
{job_description}

Provide your analysis in the exact format above with the specified headings.
"""