# project_covid

covid data plotting using django, react and redis

## project plan and requirements

Thinking of implementing the following type of flow for the covid data plotting

* react for front-end
* django for backend

```

++++++++++     ++++++++++
|        |     |        |
|        |     |        |  # here django works as api for react
| react  | <-- |django  |  # we'll be using redis streams for constant data streaming
|        |     |backend |  # for data storing we'll use sqlite db for now
++++++++++     ++++++++++
```
