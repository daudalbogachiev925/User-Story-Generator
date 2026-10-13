from templates import STORIES

def render_story(story, index):
    lines = []
    lines.append(f"### US-{index:03d}")
    lines.append(f"**As a** {story['role']},  ")
    lines.append(f"**I want** {story['action']},  ")
    lines.append(f"**So that** {story['benefit']}.")
    lines.append("")
    lines.append("**Acceptance Criteria:**")
    for ac in story["ac"]:
        lines.append(f"- [ ] {ac}")
    lines.append("")
    return "\n".join(lines)

def generate(category=None):
    result = []
    idx = 1
    for cat, stories in STORIES.items():
        if category and cat != category:
            continue
        for s in stories:
            result.append(render_story(s, idx))
            idx += 1
    return "\n".join(result)
