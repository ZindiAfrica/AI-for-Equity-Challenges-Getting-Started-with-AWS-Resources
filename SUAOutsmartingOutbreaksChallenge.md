# Outsmarting Outbreaks Challenge

## Can you turn the tide on waterborne diseases by predicting the next outbreak in Tanzania?

### Competition description

In Tanzania, waterborne diseases such as typhoid, amoebiasis, diarrhoea, schistosomiasis, and intestinal worms pose significant health risks, particularly for vulnerable populations like women and children. These diseases are exacerbated by poor water quality, inadequate sanitation, and changing climate patterns, disproportionately affecting communities with limited access to healthcare and overloading under-resourced clinics. The lack of predictive tools hinders timely interventions and prevents proper public health planning, leaving these populations without the health infrastructure they need when an outbreak occurs.

The objective of this challenge is to develop a machine learning model that can predict the outbreaks of climate-sensitive waterborne diseases. Using data on water sources, toilet quality, waste management, health facility data, and weather information from 2019 to 2023, you are tasked with predicting the extent of a waterborne disease outbreak in the Morogoro district of Tanzania.

The improved predictive capability provided by your models will enable governments and health organisations to implement timely, targeted interventions and optimise resource allocation, ultimately reducing disease incidence and enhancing public health resilience.

_This is one of two winning projects supported by the [AI For Equity Challenge](https://zindi.africa/partner/aws-ai-for-equity-challenge), in partnership with IRCAI and AWS. Sokoine University of Agriculture will have support from AWS to implement and deploy the solutions developed during this challenge._

### Data

The train set contains information from 2019 to 2022, the test set is 2023.

The objective of this competition is to predict the number of disease outbreaks, for each age group, per disease, for each month of 2023, and for each hospital.

You are provided with a climate dataset from 2019 to 2024 in csv format, you can find this dataset at [https://aws.amazon.com/marketplace/pp/prodview-odbyslwbqynos#overview](https://aws.amazon.com/marketplace/pp/prodview-odbyslwbqynos#overview) \[ASDI link to dataset\]. Other important provided datasets are locations for hospitals, toilets, waste management dumpsites and water sources.

Please note, locations and names have been masked to preserve anonymity of the vulnerable communities.

### Additional Resources

In order to support participation in this challenge, AWS has made additional resources available for participants. \[The top 100 teams to sign up to this challenge will receive AWS VM Jupyter notebook with a RTX3090 GPU with 32GB of RAM.100 people, INCLUDE QUALIFYING CRITERIA\]

DETAILS, RESOURCES, GUIDANCE

### Prizes

1st place: \$6,000 USD \& \$15,000 USD AWS Credits

2nd place: \$4,000 USD \& \$7,500 USD AWS Credits

3rd place: \$2,500 USD \& \$2,500 USD AWS Credits

There are 7,000 Zindi points available. You can read more about [Zindi points here](https://zindi.africa/discussions/13959?utm_source=zindi&utm_medium=blog&utm_campaign=challenge_resources&utm_id=CR).

### Evaluation

The evaluation for this challenge is Mean Absolute Error.

Your submission file needs to contain 2 columns: ID and Target

Here is an example of your submission.

| ID                              | Target |
| ------------------------------- | ------ |
| Location_1_x_KE_1m_2401_Typhoid | 10     |
| Location_1_x_ME_1m_2401_Typhoid | 2      |

### Resources

### About the organisation(s)

- Organisation name
- Organisation logo
- Organisation paragraph/blurb

**About Sokoine University of Agriculture ([https://www.sua.ac.tz/](https://www.sua.ac.tz/))**

Sokoine University of Agriculture (SUA) is a public University based in Morogoro Tanzania. The university is located on the slopes of the Uluguru mountains.

SUA is best known for offering courses and programmes widely in the fields of Agriculture, Veterinary Science, Forestry, Animal Science, Wildlife Management, Tourism Management, Environmental Science, Food Science, Natural Resources, Nutrition, Rural Development, since its establishment.

**About AWS ([https://aws.amazon.com/?nc2=h_lg](https://aws.amazon.com/?nc2=h_lg))**

Since launching in 2006, Amazon Web Services has been providing world-leading cloud technologies that help any organization and any individual build solutions to transform industries, communities, and lives for the better.

As part of [Amazon](https://www.aboutamazon.com/about-us), we strive to be Earth’s most customer-centric company. We work backwards from our customers’ problems to provide them with cloud infrastructure that meets their needs, so they can reinvent continuously and push through barriers of what people thought was possible.

Whether they are entrepreneurs launching new businesses, established companies reinventing themselves, non-profits working to advance their missions, or governments and cities seeking to serve their citizens more effectively—our customers trust AWS with their livelihoods, their goals, their ideas, and their data.

**About IRCAI ([https://ircai.org/vision/](https://ircai.org/vision/))**

International Research Centre on Artificial Intelligence’s strategies are to conduct theoretical and applied research in the field of artificial intelligence and advanced digital technologies, develop open solutions to help achieve Sustainable Development Goals with specific focus on SDGs 4, 5, 8, 9, 10, 13, 16 and 17, provide policy support to help Member States address the technical, legal, social and ethical challenges at the intersection of technology and policy, and provide training for upstream and downstream capacity enhancement for artificial intelligence.

### Rules

**Languages and tools:** You may only use open-source languages and tools in building models for this challenge.

**Who can compete:** Open to all

**Submission Limits:** 10 submissions per day, 300 submissions overall.

**Team size:** Max team size of 4

**Public-Private Split:** Zindi maintains a public leaderboard and a private leaderboard for each challenge. The Public Leaderboard includes approximately 30% of the test dataset. The private leaderboard will be revealed at the close of the challenge and contains the remaining 70% of the test set.

**Data Sharing:** CC-BY SA 4.0 license

**Code Review:** Top 10 on the private leaderboard will receive an email requesting their code at the close of the challenge. You will have 48 hours to submit your code.

**Code sharing:** Multiple accounts, or sharing of code and information across accounts not in teams, is not allowed and will lead to disqualification.

ENTRY INTO THIS CHALLENGE CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL CHALLENGE RULES.

**Full Challenge Rules**

This challenge is open to all.

**Teams and collaboration**

You may participate in challenges as an individual or in a team of up to four people. When creating a team, the team must have a total submission count less than or equal to the maximum allowable submissions as of the formation date. A team will be allowed the maximum number of submissions for the challenge, minus the total number of submissions among team members at team formation. Prizes are transferred only to the individual players or to the team leader.

Multiple accounts per user are not permitted, and neither is collaboration or membership across multiple teams. Individuals and their submissions originating from multiple accounts will be immediately disqualified from the platform.

Code must not be shared privately outside of a team. Any code that is shared, must be made available to all challenge participants through the platform. (i.e. on the discussion boards).

The Zindi data scientist who sets up a team is the default Team Leader but they can transfer leadership to another data scientist on the team. The Team Leader can invite other data scientists to their team. Invited data scientists can accept or reject invitations. Until a second data scientist accepts an invitation to join a team, the data scientist who initiated a team remains an individual on the leaderboard. No additional members may be added to teams within the final 5 days of the challenge or last hour of a hackathon.

The team leader can initiate a merge with another team. Only the team leader of the second team can accept the invite. The default team leader is the leader from the team who initiated the invite. Teams can only merge if the total number of members is less than or equal to the maximum team size of the challenge.

A team can be disbanded if it has not yet made a submission. Once a submission is made individual members cannot leave the team.

All members in the team receive points associated with their ranking in the challenge and there is no split or division of the points between team members.

**Datasets and packages**

The solution must use publicly-available, open-source packages only.

You may use only the datasets provided for this challenge. Automated machine learning tools such as automl are not permitted.

You may use pretrained models as long as they are openly available to everyone.

You are allowed to access, use and share challenge data for any commercial, non-commercial, research or education purposes, under a CC-BY SA 4.0 license.

You must notify Zindi immediately upon learning of any unauthorised transmission of or unauthorised access to the challenge data, and work with Zindi to rectify any unauthorised transmission or access.

Your solution must not infringe the rights of any third party and you must be legally entitled to assign ownership of all rights of copyright in and to the winning solution code to Zindi.

**Submissions and winning**

You may make a maximum of 10 submissions per day.

You may make a maximum of 300 submissions for this challenge.

Before the end of the challenge you need to choose 2 submissions to be judged on for the private leaderboard. If you do not make a selection your 2 best public leaderboard submissions will be used to score on the private leaderboard.

During the challenge, your best public score will be displayed regardless of the submissions you have selected. When the challenge closes your best private score out of the 2 selected submissions will be displayed.

Zindi maintains a public leaderboard and a private leaderboard for each challenge. The Public Leaderboard includes approximately 20% of the test dataset. While the challenge is open, the Public Leaderboard will rank the submitted solutions by the accuracy score they achieve. Upon close of the challenge, the Private Leaderboard, which covers the other 80% of the test dataset, will be made public and will constitute the final ranking for the challenge.

Note that to count, your submission must first pass processing. If your submission fails during the processing step, it will not be counted and not receive a score; nor will it count against your daily submission limit. If you encounter problems with your submission file, your best course of action is to ask for advice on the Competition’s discussion forum.

If you are in the top 10 at the time the leaderboard closes, we will email you to request your code. On receipt of email, you will have 48 hours to respond and submit your code following the Reproducibility of submitted code guidelines detailed below. Failure to respond will result in disqualification.

If your solution places 1st, 2nd, or 3rd on the final leaderboard, you will be required to submit your winning solution code to us for verification, and you thereby agree to assign all worldwide rights of copyright in and to such winning solution to Zindi.

If two solutions earn identical scores on the leaderboard, the tiebreaker will be the date and time in which the submission was made (the earlier solution will win).

The winners will be paid via bank transfer, PayPal if payment is less than or equivalent to $100, or other international money transfer platform. International transfer fees will be deducted from the total prize amount, unless the prize money is under $500, in which case the international transfer fees will be covered by Zindi. In all cases, the winners are responsible for any other fees applied by their own bank or other institution for receiving the prize money. All taxes imposed on prizes are the sole responsibility of the winners. The top winners or team leaders will be required to present Zindi with proof of identification, proof of residence and a letter from your bank confirming your banking details. Winners will be paid in USD or the currency of the challenge. If your account cannot receive US Dollars or the currency of the challenge then your bank will need to provide proof of this and Zindi will try to accommodate this.

Please note that due to the ongoing Russia-Ukraine conflict, we are not currently able to make prize payments to winners located in Russia. We apologise for any inconvenience that may cause, and will handle any issues that arise on a case-by-case basis.

Payment will be made after code review and sealing the leaderboard.

You acknowledge and agree that Zindi may, without any obligation to do so, remove or disqualify an individual, team, or account if Zindi believes that such individual, team, or account is in violation of these rules. Entry into this challenge constitutes your acceptance of these official challenge rules.

Zindi is committed to providing solutions of value to our clients and partners. To this end, we reserve the right to disqualify your submission on the grounds of usability or value. This includes but is not limited to the use of data leaks or any other practices that we deem to compromise the inherent value of your solution.

Zindi also reserves the right to disqualify you and/or your submissions from any challenge if we believe that you violated the rules or violated the spirit of the challenge or the platform in any other way. The disqualifications are irrespective of your position on the leaderboard and completely at the discretion of Zindi.

Please refer to the FAQs and Terms of Use for additional rules that may apply to this challenge. We reserve the right to update these rules at any time.

**Reproducibility of submitted code**

If your submitted code does not reproduce your score on the leaderboard, we reserve the right to adjust your rank to the score generated by the code you submitted.

If your code does not run you will be dropped from the top 10. Please make sure your code runs before submitting your solution.

Always set the seed. Rerunning your model should always place you at the same position on the leaderboard. When running your solution, if randomness shifts you down the leaderboard we reserve the right to adjust your rank to the closest score that your submission reproduces.

Custom packages in your submission notebook will not be accepted.

You may only use tools available to everyone i.e. no paid services or free trials that require a credit card.

**Documentation**

- A README markdown file is required
- It should cover:
  - How to set up folders and where each file is saved
  - Order in which to run code
  - Explanations of features used
  - Environment for the code to be run (conda environment.yml file or an environment.txt file)
  - Hardware needed (e.g. Google Colab or the specifications of your local machine)
  - Expected run time for each notebook. This will be useful to the review team for time and resource allocation.

Your code needs to run properly, code reviewers do not have time to debug code. If code does not run easily you will be bumped down the leaderboard.

**Consequences of breaking any rules of the challenge or submission guidelines:**

- First offence: No prizes for 6 months and 2000 points will be removed from your profile (probation period). If you are caught cheating, all individuals involved in cheating will be disqualified from the challenge(s) you were caught in and you will be disqualified from winning any challenges for the next six months and 2000 points will be removed from your profile. If you have less than 2000 points to your profile your points will be set to 0.
- Second offence: Banned from the platform. If you are caught for a second time your Zindi account will be disabled and you will be disqualified from winning any challenges or Zindi points using any other account.

Teams with individuals who are caught cheating will not be eligible to win prizes or points in the challenge in which the cheating occurred, regardless of the individuals’ knowledge of or participation in the offence.

Teams with individuals who have previously committed an offence will not be eligible for any prizes for any challenges during the 6-month probation period.

**Monitoring of submissions**

We will review the top 10 solutions of every challenge when the challenge ends.

We reserve the right to request code from any user at any time during a challenge. You will have 24 hours to submit your code following the rules for code review (see above). Zindi reserves the right not to explain our reasons for requesting code. If you do not submit your code within 24 hours you will be disqualified from winning any challenges or Zindi points for the next six months. If you fall under suspicion again and your code is requested and you fail to submit your code within 24 hours, your Zindi account will be disabled and you will be disqualified from winning any challenges or Zindi points with any other account.
