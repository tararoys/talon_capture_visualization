
import sys, os
import re

def open(capture_name: str, indent: str):
    # old version
    indent += '   ' 
    current_capture_rule = registry.decls.captures[capture_name].default_impl.rule.rule
    print(indent + capture_name + " -----> " + current_capture_rule)
    capture_list = re.findall('\\<(.*?)\\>', current_capture_rule)
    if len(capture_list) == 0:
        return  registry.decls.captures[capture_name].default_impl.rule.rule
    for capture in capture_list:
        if 'user' in capture: 
            yikes = open(capture, indent)
            current_capture_rule = current_capture_rule.replace('<'+ capture + '>', yikes, 1)
        elif 'self' in capture: 
            capture = capture.replace('self', 'user')
            yikes = open(capture, indent)
            capture = capture.replace('user', 'self')
            current_capture_rule = current_capture_rule.replace('<'+ capture + '>', yikes, 1)
    return str(current_capture_rule)


# def open_command(command_rule: str, indent: str):
#     # old version
#     indent += '   ' 
#     current_capture_rule = command_rule
#     current_capture_rule = re.sub(r'>\s*<', '>&<',  current_capture_rule)
#     print(indent + command_rule + " -----> " + current_capture_rule)
#     capture_list = re.findall('\\<(.*?)\\>', current_capture_rule)
#     if len(capture_list) == 0:
#         return  command_rule
#     for capture in capture_list:
#         if 'user' in capture: 
#             yikes = open(capture, indent)
#             current_capture_rule = current_capture_rule.replace('<'+ capture + '>', yikes, 1)
#         elif 'self' in capture:
#             capture = capture.replace('self', 'user')
#             yikes = open(capture, indent)
#             capture = capture.replace('user', 'self')
#             current_capture_rule = current_capture_rule.replace('<'+ capture + '>', yikes, 1)
#     return str(current_capture_rule)


def select_box_html(list_name):
    m = list_name.group(1)
    littlestr = "</td><td><select>"
    for key, value in dict(registry.lists[m][0]).items():
        littlestr += "<option >{}</option>".format(key)
        
    littlestr += "</select></td><td>"
    return littlestr


# #failed experiment with nested tables.  Tables don't nest recursively very well. 
# def capture_to_html_with_tables(capture_name, capture: str):
#     html = "<!DOCTYPE html> <head> </head> <body> <h1>" + capture_name + "</h1>  " 
#     html = html + '<table> <tbody> <tr><td> '
#     capture = capture.replace('|', '</td> </tr>  <tr><td>')
#     capture = capture.replace('(', '</td> <td> <table><tbody><tr><td> ')
#     capture = capture.replace(')', ' </td></tr></tbody></table></td><td>')
#     capture = capture.replace('[', '</td><td> [ </td> <td>')
#     capture = capture.replace(']', '</td> <td> ] </td><td>')
#     capture = capture.replace('&', '</td> <td>')
#     capture = capture.replace('<number_small>', '</td><td> &lt; number_small &gt;</td><td>')
#     capture = capture.replace('self', 'user' )
#     capture = re.sub('\\{(.*?)\\}', select_box_html, capture) 
#     html = html + capture +   '</td></tr></tbody></table></body> </html>'
#     return str(html)


#nested divs. 
def capture_to_html(capture_name, capture: str):

    style = """<style>.tr{display:block;border:solid #00f 5px;border-radius:10px;padding:2px;margin:2px}.table{border:solid #000 5px;border-radius:10px;margin:5px}.td{display:inline-block;vertical-align:top}</style>"""
    explain = "<p>  This whole sheet represents every command pattern possible under the <cursorless.target> capture.  Each blue row represents an individual command pattern.  Pick a blue row, and start reading from left to right.  When you run into a dropdown menu, pick a word off the menu.  If something is encased in [] braces, it is optional.  If something is followed by a +, that means you have to say it one or more times. If you see a stack of blue items, choose only one item from the stack to read. Keep going from left to right until you run out of things on that row. </p> "
    html = "<!DOCTYPE html>"+ style+ " <head> </head> <body> <h1>" + capture_name + "</h1>  "  + explain
    html = html + '<div class="table"> <div class="tr"><div class="td"> '
    capture = capture.replace('|', '</div> </div>  <div class="tr"><div class="td">')
    capture = capture.replace('(', '</div> <div class = "td"> <div class="table"><div class="tr"><div class="td"> ')
    capture = capture.replace(')', ' </div></div></div></div><div class="td">')
    capture = capture.replace('[', '</div><div class="td"> [ </div> <div class="td">')
    capture = capture.replace(']', '</div> <div class="td"> ] </div><div class="td">')
    capture = capture.replace('&', '</div> <div class="td">')
    capture = capture.replace('<number_small>', '</div><div class="td"> &lt; number_small &gt;</div><div class="td">')
    capture = capture.replace('self', 'user' )
    capture = re.sub('\\{(.*?)\\}', select_box_html, capture) 
    html = html + capture +   '</div></div></div></body> </html>'
    return str(html)


capture_to_html('user.cursorless_target', open('user.cursorless_target', ''))


# capture_to_html('&lt;user.cursorless_action_or_vscode_command&gt; &lt;user.cursorless_target&gt;', open_command('<user.cursorless_action_or_vscode_command> <user.cursorless_target>', ''))