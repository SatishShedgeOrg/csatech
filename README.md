# Customer scenario
Let’s take a look at the customer scenario: "Our security team is asking for help ensuring proper reviews are being done to code being added into our repositories. We have hundreds of repositories in our organization. What is the best way we can achieve at scale? We are new to some of the out-of-the-box settings and the GitHub API. Can you please help us create a solution that will accomplish this for our security team?"

# High-Level Solution Summary
## Customer should leverage GitHub advance security features, along with some of other best practices
- Code Security configuration would help with Secret scanning and also blocking commits by Push Protection
- Code scanning with CodeQL default configuration automatically detects vulnerabilities and coding errors
- Dependency graph would give details about vulnerabilities with dependencies and also auto remediation by security updates.
- Private vulnerability reporting: Allow your community to privately report potential security vulnerabilities in public repositories
- GitHub API and webhook to leverage alerts integration
- Repository Rulesets for enforcing Branch protection
- Organization Team and events for notifying team or individual about code review


# GitHub Advanced Security in the software development lifecycle

![/Users/satishshedge/Desktop/csatech/csatech/images/SecurityAudit.png](https://github.com/SatishShedgeOrg/csatech/blob/main/images/SecurityAudit.png)

This example illustrates a traditional security as a gate approach in which a single security test or a series of security tests take place during the quality-assurance phase. In this scenario, security usually ends up being a bottleneck to shipping the software. This situation is what your company wants to fix by shifting security left.

Now let's look at the same software development lifecycle with GitHub Advanced Security.

![/Users/satishshedge/Desktop/csatech/csatech/images/Security.png](https://github.com/SatishShedgeOrg/csatech/blob/main/images/Security.png)

In this scenario, security is set up right from the beginning through security policies at the project configuration stage. Developers are alerted of potential security issues at every step of the development process:

Code scanning: Scans at every commit and merge for potential vulnerabilities and coding errors.
Secret scanning: Scans at every commit and merge for tokens and private keys that were accidentally committed.
Dependency review: Keeps track of the project dependency changes and their effect on project security. It compares the repository manifest files to the databases of known vulnerabilities at every pull request.


# Some of Useful links to get more details on GitHub features
Using GitHub's security features to [secure your use of GitHub Actions]
(https://docs.github.com/en/actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions).

[REST API endpoints for secret scanning]
(https://docs.github.com/en/rest/secret-scanning/secret-scanning?apiVersion=2022-11-28).

[REST API endpoints for code scanning]
(https://docs.github.com/en/rest/code-scanning/code-scanning?apiVersion=2022-11-28).

[Configuring code scanning]
(https://docs.github.com/en/enterprise-server@3.3/admin/code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#prerequisites-for-code-scanning).

[Enabling GitHub Advanced Security]
(https://docs.github.com/en/enterprise-server@3.3/admin/code-security/managing-github-advanced-security-for-your-enterprise/enabling-github-advanced-security-for-your-enterprise).

[Configuring secret scanning]
(https://docs.github.com/en/enterprise-server@3.3/admin/code-security/managing-github-advanced-security-for-your-enterprise/configuring-secret-scanning-for-your-appliance).

[Enabling Dependabot]
(https://docs.github.com/en/enterprise-server@3.3/admin/configuration/configuring-github-connect/enabling-dependabot-for-your-enterprise).