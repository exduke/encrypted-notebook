export default function download(blob, filename){
    let a = document.createElement('a')
    a.style.display = 'none'
    a.href = URL.createObjectURL(blob)
    a.download = filename
    // link.target = "_blank"
    document.body.appendChild(a)
    a.click()
    URL.revokeObjectURL(a.href)
    document.body.removeChild(a)
}
