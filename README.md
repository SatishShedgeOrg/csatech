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


