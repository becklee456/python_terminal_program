

let Task= [
    {id:1,title:"learn next.js routes",completed:false},
    {id:2,title:"lern next.js api creation",completed:true}
]

export async function GET() {
    return Response.json(Task)
}