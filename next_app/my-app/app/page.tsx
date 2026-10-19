import React, { useState } from 'react'

interface Task{
  id:number;
  title:string;
  completed:boolean
}
export default function page(){
  const [task,setTask]=useState(<Task[]>);

  const loadTask=async()=>{
      const res=await fetch("/api/task");
      const data=await res.json()
  }
  return (
    <div>
      <h1>welcome</h1>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          {/* <li><a href="/about">About</a></li> */}
          <li><a href="/users">users</a></li>
        </ul>
      </nav>
    </div>
  )
}
