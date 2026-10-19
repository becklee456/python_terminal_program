import React from 'react'


interface User{
    id:string;
    name:string,
    email:string
}
async function page() {
    const res=await fetch("https://jsonplaceholder.typicode.com/users")
    const data=await res.json() as User[];
   
  return (
    <div>
        <h1 className="text-5xl capitalize">users page</h1>

        <table>
            <thead>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>email</th>
                </tr>
            </thead>

            <tbody>
                {data.map((d)=>(
                    <tr key={d.id}>
                       <td>{d.id}</td>
                       <td>{d.name}</td>
                       <td>{d.email}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
  )
}

export default page