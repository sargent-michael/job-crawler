# WEB CRAWLER

This program searches the Palo Alto job site on a specific filter, find the job link url, and then pulls the job link description out of that url.

The output of the program is suppose to look like the data below, however, I am trying to make it look better:

```python
python3 web.py 
--------------------------------------------------
Job Title: Security Researcher (Web Security) 
Link: https://jobs.paloaltonetworks.com/en/jobs/job/security-researcher-web-security-santa-clara-2298f14a-816f-426e-b4f2-a82ae28842f5/ 
--------------------------------------------------

Description
  Our Mission    At Palo Alto Networks® everything starts and ends with our mission:   Being the cybersecurity partner of choice, protecting our digital way of life.   We have the vision of a world where each day is safer and more secure than the one before. These aren’t easy goals to accomplish – but we’re not here for easy. We’re here for better. We are a company built on the foundation of challenging and disrupting the way things are done, and we’re looking for innovators who are as committed to shaping the future of cybersecurity as we are.   We’re changing the nature of work. Palo Alto Networks is evolving to meet the needs of our employees now and in the future through FLEXWORK, our approach to how we work. From benefits to learning, location to leadership, we’ve rethought and recreated every aspect of the employee experience at Palo Alto Networks.  And because it FLEXes around each individual employee based on their individual choices, employees are empowered to push boundaries and help us all evolve, together.    Your Career    The Web Security Research team is responsible for delivering high quality content to our products to prevent successful cyberattacks and protect our customers, with a special focus on malicious URL detection, DNS security, network security and privacy protection.    We are looking for a motivated and creative Principal Security Researcher to join our team to research, design, and develop innovative threat detection systems and infrastructure for protecting customers against constantly evolving online threats and attacks.
```