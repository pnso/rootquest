# RootQuest

RootQuest is your training ground for real-world cybersecurity skills. Download labs, exploit vulnerabilities, learn by doing.

## 🔍 What is RootQuest?

RootQuest is a collection of hands-on, containerized cybersecurity labs. Built for learners, hobbyists, and students who want real-world practice in system exploitation.

- Labs run in Docker containers locally
- Each lab includes a challenge, walkthrough, and flag
- No login, no setup hell, just clone, run, and hack

## 📦 Labs Available

- `sudo-less-lab`: Exploit misconfigured sudo access to `less` for privilege escalation.

More labs coming soon...

## ⚙️ How to Run a Lab

```bash
cd labs/sudo-less-lab
docker build -t sudo-less-lab .
docker run -it --rm sudo-less-lab
```
