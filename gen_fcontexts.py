import semanage

handle = semanage.semanage_handle_create()
semanage.semanage_connect(handle)

(_, fclist) = semanage.semanage_fcontext_list(handle)

for fcontext in fclist:
    expr = semanage.semanage_fcontext_get_expr(fcontext)
    con = semanage.semanage_fcontext_get_con(fcontext)
    if con:
        (_, con_str) = semanage.semanage_context_to_string(handle, con)
        print("(%r, %r)," % (expr, con_str))
