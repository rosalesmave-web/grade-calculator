# Git Reflection: Resolving a Merge Conflict

**Student:** John Maverick Rosales  
**Topic:** Resolving a Git Merge Conflict During Branch Integration  

---

### Reflection

While working on this grade calculator project, one major challenge I encountered was handling a Git merge conflict when integrating my feature branch back into main. Before initiating the merge, I had made localized adjustments to the menu options directly on main while simultaneously restructuring the control loop in my feature branch. When I executed git merge, Git halted the process, warning that automatic merge had failed due to overlapping modifications in grade_calculator.py.

At first, seeing conflict markers was intimidating because I was concerned about losing newly implemented logic. To resolve this, I opened the affected file in my code editor, carefully compared the conflicting code blocks, and manually unified the changes—preserving both the updated weighted calculations and the new statistical reporting functions. Afterward, I staged the resolved file using git add and finalized the integration with git commit. This experience taught me the importance of inspecting file diffs with git status and git diff, as well as maintaining clear, modular code commits to avoid merge collisions.
