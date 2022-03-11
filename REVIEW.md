###### Review 1 by Satwik Goyal
1. Documentation: I think the README file is very well written to setup the backend. The comments in the code files are great as well!
2. Version Control: I believe you had made great use of version control and each commit has well written decriptions.
3. Naming Conventions: I think the naming convention used are great and very intuitive.
4. Modularity: You have done a great job at decomposing the code into seperate code files.
5. Testability: I didn't see any tests (please let me know if I missed them). Maybe adding a few test cases could make the code more robust/ready.

Final Note: Honestly I don't have much experience with backend so I cannot give any technical feedback on the code. 
However, from a software engineering perspective this code follows all best pratices. Maybe adding a few test cases might help (although
I am not sure how testing works for the backend). 
###### Review 1 ends here

###### Review 2 by Yugantar Prakash

Documentation and preliminaries: Overall done well. Got the following error when running ```alembic upgrade head```:
```
ModuleNotFoundError: No module named 'psycopg2'
```
Of course that's a simple fix, but recommended to add this to READ.md

Similarly, recommended to add basic instructions to installing Docker-Compose on top of Docker, as well as to make sure it is the right version. Of course, these recommendations are coming from someone with no prior experience working with Dockers.

Code review: Modularity of the code is done well! Good commenting practice and naming convention followed!
###### Reivew 2 ends here