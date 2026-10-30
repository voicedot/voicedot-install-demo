# Workshop Notes — Voicedot installation demo

A small fictional website for showing an agent-assisted Voicedot installation,
from a website with no widget to a working project and a real first message.

Publisher: **Good Sheet Sp z o.o.** Source code is MIT licensed.

Planned public URL: https://voicedot.github.io/voicedot-install-demo/

This is separate from the completed feedback-to-code example at
https://review.voicedot.ai/ and its source repository,
https://github.com/voicedot/voicedot-review-demo.

## What's here

- `site/`: plain HTML, CSS, and a small script showing the deployed revision.
- `scripts/build_site.py`: copies the static site and stamps its exact commit.
- `.github/workflows/publish.yml`: validates and deploys `main` to GitHub Pages.
- No build dependencies, customer data, credentials, analytics, or external fonts.

The initial version deliberately has **no Voicedot snippet and no project binding**.
The coding agent adds them during the installation demonstration, after consent.
The public widget site ID may appear in source; private installation credentials,
email links and CLI state must stay outside this repository.

## Preview

```sh
python3 -m http.server 4472 --directory site --bind 127.0.0.1
```

This local preview is only for development. The installation recording must use
the actual public deployment and a fresh accepted backend ping.

## Recording sequence

1. Show the published website before installation.
2. Ask the coding agent to register and install Voicedot with the agreed email.
3. Review the account/delegation consent checkpoint outside confidential footage.
4. Complete email verification off camera. Never show the magic link.
5. Show the real source change and deployment.
6. Open the exact public URL and verify a new backend installation ping.
7. The human sends their first message and chooses their plan.

The agent does not select a plan, make a purchase, mark a human review decision,
or silently treat its own test message as the human onboarding milestone.

## Publish and verify

Pushing `main` publishes the demo. Run `python3 scripts/build_site.py --commit SHA`
before publishing, inspect the change, and check the result in a real browser.
After deployment, match `deployment.json` to the pushed commit. A Git push alone
does not prove that installation or deployment succeeded.
