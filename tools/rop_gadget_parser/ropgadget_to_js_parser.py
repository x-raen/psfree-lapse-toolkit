import re

def parse_ropgadget_output_to_js_map(ropgadget_output_file, map_variable_name="auto_generated_gadget_offsets"):
    """
    Parses the output of ROPgadget and generates a JavaScript Map string.

    Args:
        ropgadget_output_file (str): Path to the ROPgadget output file.
        map_variable_name (str): The name for the JavaScript Map variable.

    Returns:
        str: A string containing the JavaScript code for the gadget Map.
    """
    gadget_entries = []
    try:
        with open(ropgadget_output_file, 'r') as f:
            # Flag to start reading gadgets after the header
            reading_gadgets = False
            for line in f:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("Gadgets information"):
                    # Skip the header line itself
                    next(f) # Skips the "====================..."
                    reading_gadgets = True
                    continue
                
                if line.startswith("Unique gadgets found:") or line.startswith("ROP chain generation"):
                    reading_gadgets = False # Stop reading if we reach the summary or ROP chain part
                    break

                if reading_gadgets:
                    # Regex to capture "0x<address> : <instruction_string>"
                    match = re.match(r'(0x[0-9a-fA-F]+)\s*:\s*(.*)', line)
                    if match:
                        address = match.group(1)
                        instruction = match.group(2).strip()
                        # Escape backslashes and double quotes for JavaScript string literal
                        escaped_instruction = instruction.replace("\\", "\\\\").replace("\"", "\\\"")
                        js_instruction_string = f'"{escaped_instruction}"'
                        gadget_entries.append(f"    {js_instruction_string} : {address},")
                    else:
                        # Lines that don't match are usually part of multi-line gadgets or other info, ignore for now
                        pass 

    except FileNotFoundError:
        return f"Error: Input file '{ropgadget_output_file}' not found."
    except Exception as e:
        return f"Error processing file: {e}"

    if not gadget_entries:
        return f"// No gadgets found or parsed from '{ropgadget_output_file}'.\nconst {map_variable_name} = new Map();"

    # Remove trailing comma from the last entry
    if gadget_entries:
        gadget_entries[-1] = gadget_entries[-1].rstrip(",")

    js_map_string = f"const {map_variable_name} = new Map(Object.entries({{\n"
    js_map_string += "\n".join(gadget_entries)
    js_map_string += "\n}}));"

    return js_map_string

if __name__ == "__main__":
    rop_output_file = "/home/ubuntu/rop_gadget_output.txt"
    generated_js_code = parse_ropgadget_output_to_js_map(rop_output_file)
    print(generated_js_code)

    # Example with a different map name
    # generated_custom_code = parse_ropgadget_output_to_js_map(rop_output_file, "custom_rop_gadgets")
    # print("\n// Example for custom_rop_gadgets")
    # print(generated_custom_code)

