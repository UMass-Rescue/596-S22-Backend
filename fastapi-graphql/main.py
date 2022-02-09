from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from schemas import CourseType
import json

class Query (ObjectType):
    course_list = None
    get_course = List(CourseType)
    async def resolve_get_course(self, info):
        with open("./courses.json") as courses:
            course_list = json.load(courses)
        return course_list

app = FastAPI()
app.add_route("/", GraphQLApp(
    schema=Schema(query=Query),
    executor_class=AsyncioExecutor
    )
)