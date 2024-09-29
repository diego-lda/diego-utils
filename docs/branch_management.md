# Branch Management

You have your data science project, your goals are clear (and prioritised).
Perhaps you even have some timelines that can guide your development plan.
In most cases you will start with some pre-existing code or some code ideas.

As discussed in [the section on Git and Sustainability](git_sustainability.md), it is important that there is a solid
version control system and strategy that can provide a comfortable and reliable framework for your data science team.

If you are uncertain what branches are and how to use Git commands to navigate them, you are definately not alone.
The [official Git Pro Book](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) is a great reference, although a bit
dense. [The Altissan explainer](https://www.atlassian.com/git/tutorials/using-branches) is much more approachable.
There are a series [GitHub articles on branching](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) that are also a good start.
For something a bit more interactive, as expected [freeCodeCamp.org](https://www.youtube.com/watch?v=e2IbNHi4uCI) have an amazing video for you.
[For those that like short-form content](https://www.youtube.com/watch?v=YyFrdoD-Wjk).
I don't aim to explain branches mechanically in detail here, but rather give my thoughts on how to use them as part of the development of a data science project.

## Key Branches (`main` and `development`)

By default, when you create a repository, there will only be one branch, the `main` or `master` branch.
However, as covered in other sections, working directly in this branch runs the risk of causing chaos if errors are pushed.
For less experienced coders or when developing new features coding directly onto the `main` branch can be daunting and discourage innovation.
Using only the `main` branch is also likely to cause issues with code conflicts when working as a team.

As such, even if you are working on your own I would always recommend setting up a `development` branch.
This can be used to test new code and once a significant amount of code has been added and sufficiently tested, it can be merged into `main`.
Following a _sprint_ or _agile_ culture may mean that merges to the `main` branch happen with a pre-scheduled frequency.
In the past, I have seen pencilling in merges at the end of sprints (couple of weeks) act as a catalyst for development and provides a nice
structure for stakeholders and performance evaluation.

## Feature Branches

If you are more than a one-person band, you will want to have more branches known as __feature branches__.
Branching out of `development`, feature branches can contain specific development threads.
Towards the end of the _sprint_ or when development on that particular feature is complete, it can be merged back into the `development` branch.
This has the benefit of compartmentalising development, without the rest of the codebase changing, applying the _'ceteris paribus'_ principle.
Once all the feature branches are merged into `development` the team can ensure integration of the diferent new features with each other in one go.
It also gives a natural place to perform housekeeping tasks, like updating the _CHANGELOG.md_ or bumping the version of the project.

### Naming Feature Branches

There is relatively established conventions on how to name branches. `some-more-updates` is not a good name.

- __New Feature Branches__: `feature-<feature_name>` for introducing new features.
- __Bug Fixes__: `fix-<bug_description>` for resolving bugs.
- __Hotfixes__: `hotfix-<issue>` for urgent fixes that go straight to production. _These should be rare!_
- __Improvements/Refactors__: `refactor-<description>` or `improvement-<description>` for code structure improvements that have minimal impact on functionality.
- __Documentation__: `docs-<change_description>` for updates to documentation.
- __Experimental__: `experiment-<experiment_name>` for trial and exploratory work.

Establishing what category out of these your work fits in isn't straight forward, and you shouldn't devote too much time thinking about this.
For example, say that you have some code that takes some data and produces some analysis.
You want to work some new data validation for the inputs. This could go under `feature-pydantic_validation` or perhaps `improvement-data_validation`.

The key benefit of following the above naming convention, even if it's not always super thought-through or consistent,
is to allow an easy (and broad) understanding of what is going on.
For example, if your data science project only has `fix-` branches and barely any `feature-` ones,
is it because you are addressing some tech debt to have a good platform to do some more development soon,
or is it because the code is of bad quality and there are loads of issues?
It also allows you to go back and analyse what topics certain people have worked on, do you have a `fix-` expert
or perhaps someone that hasn't had the chance to do some  some `experiment-` work in a while?
The `<description>` part is also useful to track where some unintended issues may have been introduced.

Both of these issues can also be identified through the use of _GitHub Issues_ or _~Jira~ tickets_.
To this effect, I have also seen branches be named after issues, for example `<issue#>-<description>`.
This isn't as straightforward to understand at first sight, but also helps make the link between issues and code.
GitHub provides some good functionality for this, so I think sticking to the standard naming convention might be the best path forward.

## Pull Requests

Once a feature branch is ready and the time to merge it back into `development` is nearing close, the peer review process should take centre stage.
Throughout the development in this feature branch, work may have been collaborative and updates may have been shared.
However, the _pull request_ provides the best platform to ensure that peer-reviews are consistent, documented and of high quality.
When the developer of the feature branch feels ready, they should raise a _pull request (PR)_.
This will flag to the rest of the development team that the work is ready for others to see it.
When raising a PR, you can nominate a reviewer as well as link any related issues that could be closed if this code where merged.

### Who should review?

I believe that all team members (regardless of their seniority) should both code (raise new PRs) and conduct peer reviews.
Code that has been developed by experienced members may provide insights for more junior coders.
It may also be rushed or incomprehensible to anyone else, something junior developers should be encouraged to point out.
Code developed by newer developers may provide new perspectives and insights and allow senior devs to keep up-to-date with the latest techniques.
It may also be a good opportunity for seniors to provide some specific feedback on development opportunities or provide some more context on the project.

### What should happen when a PR is raised

Pull requests provide a great example of when GitHub Actions can make your teams data science less admin-based as well as more consistent.
Setting up a Pull Request GitHub Action is really straight forward. This project has one set up you can take and run with.
On the one hand, they can provide a template for the pull request, during creation, that presents the raiser with a checklist on the work
completed and on what is expected from the reviewer. This can be a great way of catching out any pull requests that haven't been tested locally
or that fail to update relevant documentation.
Moreover, GitHub Actions can be set up to automatically check for documentation updates as well as testing the code in an automated way.
This ensures the easy identification of new bugs before they are merged to `main` as well as providing a backstop for the reviewer.
Saving them reviewing half-baked code and having to go back-and-forth with the developer too many times.

### Conducting a Review of a PR

Talk about the peer review checklist, to centre the discussion.