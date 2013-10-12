
import errno
import imp
import os

from jinja2 import Environment, FileSystemLoader
from optparse import OptionParser


def render_template(input_file, output_file, context):
    path = os.path.dirname(input_file)
    template_name = os.path.basename(input_file)

    loader = FileSystemLoader(searchpath=path, encoding='utf-8')
    env = Environment(loader=loader, trim_blocks=True)

    template = env.get_template(template_name)
    data = template.render(**context)
    with open(output_file, 'w') as f:
        f.write(data.encode('utf-8'))


def makedirs(path, mode=0777):
    try:
        os.makedirs(path, mode)
    except OSError as e:
        if e.errno==errno.EEXIST and os.path.isdir(path) and os.access(path, os.R_OK | os.W_OK | os.X_OK):
            return
        raise


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--input', help='Input template file')
    parser.add_option('--output', help='Output file')
    parser.add_option('--context', help='File with template context')

    options, args = parser.parse_args()

    if not options.input or not os.path.isfile(options.input):
        raise RuntimeError('Invalid input file specified: %s' % options.input)

    if not options.output:
        raise RuntimeError('Output file must be specified')

    out_path = os.path.dirname(options.output)
    if out_path:
        makedirs(out_path)

    ctx_mod = imp.load_source('jcfg.context', options.context)
    options.context = getattr(ctx_mod, 'context', {})

    render_template(options.input, options.output, options.context)

