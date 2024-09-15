class NoteBookNode {
    constructor(title, content, children) {
        this.title = title
        this.content = content
        this.children = children
        this.chosen = false
    }

    toJsonObj() {
        let children = []
        for (let i in this.children) {
            children.push(this.children[i].toJsonObj())
        }
        return [this.title, this.content, children]
    }

    fromJsonObj(obj) {
        this.title = obj[0]
        this.content = obj[1]
        for (let i in obj[2]) {
            let node = new NoteBookNode('', '', [])
            node.fromJsonObj(obj[2][i])
            this.children.push(node)
        }
    }

    find(keys) {
        if (keys.length) {
            let key = keys.shift()
            return this.children[key].find(keys)
        }
        else
            return this
    }
}

export default class NoteBookObj {
    constructor() {
        this.root = new NoteBookNode('', '', [])
        this.root.chosen = true
        this.chosenNodeKeys = []
    }

    fromJsonObj(obj) {
        this.root.fromJsonObj(obj)
    }

    toJsonObj() {
        return this.root.toJsonObj()
    }

    find(keys) {
        return this.root.find([].concat(keys))
    }

    choose(keys){
        this.find(this.chosenNodeKeys).chosen = false
        this.chosenNodeKeys = [].concat(keys)
        this.find(keys).chosen = true
    }

    add(keys){
        if (keys==undefined)
            keys = this.chosenNodeKeys
        this.find(keys).children.push(new NoteBookNode('','',[]))
    }

    remove(keys){
        if (keys==undefined)
            keys = [].concat(this.chosenNodeKeys)
        let key = keys.pop()
        this.choose(keys)
        this.find(keys).children.splice(key, 1)
    }
}