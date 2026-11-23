#!/usr/bin/env node
// Install the overseas-web-seo skill into an agent's skills directory.
// Zero dependencies: copies SKILL.md, references/ and scripts/ into place.

import { cp, mkdir, stat } from 'node:fs/promises';
import { homedir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const pkgRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);

function valueAfter(flag) {
  const at = args.indexOf(flag);
  return at === -1 ? undefined : args[at + 1];
}

if (args.includes('--help') || args.includes('-h')) {
  console.log(`Usage: npx overseas-web-seo [--dir <skills-dir>]

  --dir <path>   Directory that holds installed skills (default: ~/.claude/skills)
                 Codex uses ~/.codex/skills, project installs use ./.claude/skills
  --help, -h     Show this message
`);
  process.exit(0);
}

const skillsDir = resolve(valueAfter('--dir') ?? join(homedir(), '.claude', 'skills'));
const target = join(skillsDir, 'overseas-web-seo');

await mkdir(target, { recursive: true });
for (const entry of ['SKILL.md', 'references', 'scripts']) {
  await cp(join(pkgRoot, entry), join(target, entry), { recursive: true });
}

const size = (await stat(join(target, 'SKILL.md'))).size;
console.log(`installed overseas-web-seo -> ${target} (SKILL.md ${size} bytes)`);
console.log('Next: ask your agent something like "帮我看下 xxx 这个词还值不值得做"');
