 <p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

 Set up your agent to use an MCP Server
 
In order to setup MCP, you will need to register the MCP server it in `endpoints.yml` so Rasa knows its address at runtime. The `name` you set here must match the `name` under `connections.mcp_servers` in the sub-agent you will configure in the next lab. 


Add the below block to the `endpoints.yml` file with the new MCP server registered:
 
```yaml

 
mcp_servers:                            # add this block
  - name: appointment_mcp
    url: http://127.0.0.1:8080/mcp      # Streamable HTTP; must include the /mcp path
    type: http
```
  
**Steps:**
 
1. Add the `mcp_servers:` block to `endpoints.yml` before `model_groups:`. Save.
2. Run the Code Test.
{Check It!|assessment}(code-output-compare-501060002)
 
