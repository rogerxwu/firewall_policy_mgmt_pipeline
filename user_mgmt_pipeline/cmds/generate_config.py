from jinja2 import Environment, FileSystemLoader
import yaml
import os

def generate_config(template_path, data_path, output_path):
    # Load the Jinja2 template environment
    env = Environment(loader=FileSystemLoader('.'))

    # Load the user template according to device vendor and type
    template = env.get_template(template_path)

    # Load the user data from YAML file
    with open(data_path) as f:
        data = yaml.safe_load(f)

    # Render the template with the user data
    rendered_template = template.render(data)

    # Write the rendered template to the output file
    with open(output_path, 'w') as f:
        f.write(rendered_template)

    print(f'Configuration generated')

if __name__ == "__main__":
    template_path = './templates/juniper/user_vsrx_template.j2'
    data_path = './user.yaml'
    output_path = './staging/user_juniper_vsrx.cfg'

    generate_config(template_path=template_path, data_path=data_path, output_path=output_path)