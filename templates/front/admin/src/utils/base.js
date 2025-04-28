const base = {
    get() {
        return {
            url : "http://localhost:8080/djangoh648w/",
            name: "djangoh648w",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/djangoh648w/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "在线购物平台"
        } 
    }
}
export default base
