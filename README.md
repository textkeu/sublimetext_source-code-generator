# SublimeText : Source Code Generator

Plugin for sublime text to get your job done faster and avoid repetitive work.

# Installation 
### Unix/Linux or MacOS
1. change folder to your SublimeText's Package folder
    - `cd ~/.config/sublime-text-3/Packages`
2. clone plugin into SublimeText's Package folder
    - `git clone https://github.com/textkeu/sublimetext_source-code-generator.git`
### Window
1. open your SublimeText application
2. From Menu, select option **Preferences** / **Browse Packages**
3. Download [Plugin](https://github.com/textkeu/sublimetext_source-code-generator) and uncompress it
4. copy or move **Folder** (at step #3) to **Packages** folder (at step #2)

# How to use
1. Make your source code template file in **SublimeText's_Package_folder**/sublimetext_source-code-generator/templates/
* For Example :  **HTML/html.tmpl**
```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title></title>
        <link rel="stylesheet" type="text/css" href="css_path.css">
    </head>
    <body>
    <script type="text/javascript" src="js_path.js"></script>
    </body>
</html>

```

2. Add template to Sublimetext's menu into **SublimeText's_Package_folder**/sublimetext_source-code-generator/Context.sublime-menu
* For Example :  
````
[{
  "caption": "Source Code Generator",
  "children": [
    {
      "caption": "HTML",
      "children": [
                {
                  "caption": "html",
                  "command": "source_code_generator",
                    "args": { "filepath": "/templates/HTML/html.tmpl"}
                }
            ]
    }
  ]
}]

````
3. Generate source code
* Click right button > hover in option **Source Code Generator**
* hover into what you want to generate

# Tips
1. For demonstration: You can copy all files and folders in folder **sample** to **SublimeText's_Package_folder**/sublimetext_source-code-generator/