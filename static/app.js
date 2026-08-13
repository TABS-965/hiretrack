function openModal(){document.getElementById("addModal").classList.add("show")}
function closeModal(){document.getElementById("addModal").classList.remove("show")}
function closeEdit(){document.getElementById("editModal").classList.remove("show")}
function editApp(id,status,notes){
 document.getElementById("editForm").action="/applications/"+id+"/update";
 document.getElementById("editStatus").value=status;
 document.getElementById("editNotes").value=notes||"";
 document.getElementById("editModal").classList.add("show");
}
function filterRows(){
 const q=document.getElementById("search").value.toLowerCase();
 const status=document.getElementById("statusFilter").value;
 document.querySelectorAll(".row").forEach(row=>{
   const matchesText=row.dataset.search.includes(q);
   const matchesStatus=status==="All statuses"||row.dataset.status===status;
   row.style.display=matchesText&&matchesStatus?"grid":"none";
 });
}
window.onclick=e=>{
 if(e.target.id==="addModal")closeModal();
 if(e.target.id==="editModal")closeEdit();
}
document.querySelectorAll(".flash").forEach(x=>setTimeout(()=>x.remove(),3500));
