const encrypt = function (e, t, n, r) {
    r = this.cfg.extend(r);
    var i = e.createEncryptor(n, r)
        , o = i.finalize(t)
        , a = i.cfg;
    return v.create({
        ciphertext: o,
        key: n,
        iv: a.iv,
        algorithm: e,
        mode: a.mode,
        padding: a.padding,
        blockSize: e.blockSize,
        formatter: r.format
    })
}
const cfg = {
    
    extend: function (e) {
        var t = a(this);
        return e && t.mixIn(e),
            t.hasOwnProperty("init") && this.init !== t.init || (t.init = function () {
                t.$super.init.apply(this, arguments)
            }
            ),
            t.init.prototype = t,
            t.$super = this,
            t
    },
}


a = {
    mixIn: function (e) {
        for (var t in e)
            e.hasOwnProperty(t) && (this[t] = e[t]);
        e.hasOwnProperty("toString") && (this.toString = e.toString)
    },
}

createEncryptor: function(e, t) {
    return this.create(1, e, t)
}