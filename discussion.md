# Mango Chat-Ne

This document outlines the current state and future development plans for our recruiting application. The aim is to enhance recruitment processes by integrating advanced AI functionalities that evaluate candidates automatically, in order to create digestible quantities of applicants (breaking it down from many hundreds to less than 10). Currently, this is done rudimentarily based on their technical and personal fit, but in the future, many more concerns can be addressed.

## Current Implementation

### Technical Fit Bot
- **Objective:** Automate the assessment of candidates' purely technical abilities relevant to the job position.
- **Status:** Implemented. Provides a baseline evaluation by analyzing candidates' skills, experience, and education.

### Personal Fit Bot
- **Objective:** Evaluate candidates' personal attributes to determine cultural and team compatibility.
- **Status:** Implemented. Assesses soft skills, values, and personality traits to predict the candidate's integration into the company culture.

## Planned Developments

### Company-Specific Requirement Bots
- **Objective:** Develop bots that rate candidates according to specific company needs and job requirements. Customization can account for gender, ethnicities, or other diversity concerns.
- **Plan:** Customize evaluation criteria based on a detailed analysis of company values, job roles, and industry standards. Add the possibility to hard-code certain quotas given by companies.

### Job Agnostic Rating for Elite Candidates
- **Objective:** Identify and highlight elite candidates regardless of the job they apply for. In case candidates apply that might have lower fit values but incredibly competitive CVs, they should have the possibility to be highlighted.
- **Plan:** Implement a scoring system that recognizes exceptional skills, achievements, and potentials that transcend specific job roles.

### Preprocessing for Lengthy CVs
- **Objective:** Manage and effectively analyze unreasonably long CVs.
- **Plan:** Create preprocessing tools that summarize and prioritize information in CVs, ensuring key qualifications and experiences are highlighted.

### Red Flag Scanner Bot
- **Objective:** Automate the identification of potential red flags in candidates' profiles and histories. E.g., current trends such as job hopping or others should be considered and highlighted.
- **Plan:** Develop a bot that scans for inconsistencies, gaps in employment, or other indicators that warrant further investigation.

### Team Shortcomings Compensation Bot
- **Objective:** Propose candidates that compensate for the existing team's shortcomings.
- **Plan:** Analyze team composition and performance to identify skill and personality gaps. The bot will prioritize candidates who fill these gaps, promoting a more balanced and effective team.

## Conclusion

Our goal is to create a comprehensive recruiting application that not only streamlines the hiring process but also ensures a high degree of match precision between candidates and job roles. By advancing our AI capabilities, we aim to offer a nuanced, efficient, and tailored recruitment solution that meets the evolving needs of our company and our teams.
