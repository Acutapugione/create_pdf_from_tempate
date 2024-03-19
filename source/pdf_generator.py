from typing import Generator, List
from jinja2 import Environment, FileSystemLoader, Template, filters
from html2text import HTML2Text
from weasyprint import HTML, CSS
from . import search_files_by_extension, format_currency


class PDFGenerator:
    environ: Environment
    stylesheets: tuple[CSS] 
    
    def __init__(self, 
                 template_folder_path: str = ".",
                 style_folder_path: str = ".",
                 environ: Environment|None = None, 
                 stylesheets:tuple[CSS|str]|None = None) -> None:
        
        self.environ = environ or Environment(loader=FileSystemLoader(template_folder_path))
        self.environ.filters['format_currency'] = format_currency
        self.stylesheets = stylesheets or [CSS(filename=file) for file in search_files_by_extension(style_folder_path, 'css')]
        
    def _render_template(self, template_name: str, **context) -> str:
        template = self.environ.get_template(template_name)
        return template.render(**context)

    def _make_html(self, html_content: str) -> HTML:
        return HTML(string=html_content)
    
    def _apply_styles(self, html: HTML) -> bytes:
        return html.write_pdf(stylesheets=self.stylesheets)

    def run(self, template_name: str, **context) -> bytes:
        return self._apply_styles(self._make_html(self._render_template(template_name, **context)))
    