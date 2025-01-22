# Kuyesera AI Disaster Damage and Displacement Challenge

**Can you help communities recover by detecting damaged infrastructure using aerial imagery?**

- **Prize**: $12,500 USD + AWS credits
- **Competition Ends**: ~1 month left
- **Helping**: Malawi
- **Focus Areas**: Object Detection, Classification, Health, Climate, Gender, Policy

---

## Description

In March 2023, Cyclone Freddy caused devastating floods in Blantyre, Malawi, leaving destruction in its wake. Vulnerabilities such as inadequate drainage, deforestation, and unregulated urban sprawl exacerbated the disaster's effects, particularly in communities like Chilobwe on Soche Mountain. Societal inequalities deepened the crisis, with women, pregnant women, and young girls facing significant recovery challenges, including loss of shelter, limited healthcare access, and prolonged displacement.

Your mission is to develop a machine learning model to identify house locations and assess damage levels caused by Cyclone Freddy.

- **Dataset**: Training on the xBD dataset and testing on a hand-labeled dataset from Kuyesera AI Lab.
- **Challenge Complexity**: Real-world post-disaster challenges are reflected in the 6-month gap between pre- and post-disaster imagery.

Data is sourced from the **Amazon Sustainability Data Initiative (ASDI)**, Amazon’s tech-for-good program supporting climate-related research. This challenge is one of two winning projects of the **AI For Equity Challenge**, in partnership with IRCAI and AWS.

### Supporting Partners

- **AWS**: World-leading cloud technologies for sustainability-related research.
- **IRCAI**: Focused on AI solutions for Sustainable Development Goals (SDGs).
- **Kuyesera AI Lab**: AI research at Malawi University of Business and Applied Sciences.

---

## Evaluation

The competition's evaluation metric is **Mean Absolute Error**.  
Submission files must include two columns: `id` and `target`.

Each image is classified into four categories:

1. Destroyed
2. Major Damage
3. Minor Damage
4. No Damage

Example submission format:

| id                                     | target |
| -------------------------------------- | ------ |
| malawi-cyclone_00000001_X_destroyed    | 0      |
| malawi-cyclone_00000001_X_major_damage | 1      |
| malawi-cyclone_00000001_X_minor_damage | 0      |
| malawi-cyclone_00000001_X_no_damage    | 5      |

---

## Additional Resources

AWS provides additional resources to participants, including AWS credits for the top 100 teams or individuals by 8 January 2025. Available tools include:

- **AWS Glue**: Data preparation and automation for satellite imagery.
- **Amazon SageMaker Data Wrangler**: Simplified workflows for satellite imagery analysis.
- **AWS Deep Learning AMIs (DLAMIs)**, **AWS Batch**, and more.

---

## Timeline

- **Competition Closes**: 31 January 2025
- **Final Submission Deadline**: 11:59 PM GMT

---

## Prizes

- **1st Place**: \$6,000 USD \& \$15,000 AWS Credits
- **2nd Place**: \$4,000 USD \& \$7,500 AWS Credits
- **3rd Place**: \$2,500 USD \& \$2,500 AWS Credits

Winning solutions must include an object identification component (e.g., centroids, boxes, or polygons). Participants must utilize at least one dataset from the Amazon Sustainability Data Initiative (ASDI).

---

Learn more and join the challenge at [Zindi Africa](https://zindi.africa/competitions/kuyesera-ai-disaster-damage-and-displacement-challenge).
