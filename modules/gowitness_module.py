from core.module import ReconModule
from core.toolrunner import ToolRunner

class GowitnessModule(ReconModule):
    
    name = "gowitness"
    
    dependencies = ["httpx"]
    
    async def run(self, context):
    
        print("[*] Running Gowitness")
    
        alive_file = (
            context.workspace
            / "http"
            / "alive_urls.txt"
        )
    
        if not alive_file.exists():
        
            print(
                "[!] alive.txt not found"
            )
    
            return
    
        output_dir = (
            context.workspace
            / "screenshots"
        )
    
        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )
    
        cmd = (
            f"gowitness scan file "
            f"-f {alive_file} "
            f"-s {output_dir}"
        )
    
        await ToolRunner.run(
            cmd
        )
    
        for image in output_dir.iterdir():
        
            if not image.is_file():
                continue
    
            if image.suffix.lower() not in [
                ".jpeg",
                ".jpg",
                ".png"
            ]:
                continue
    
            context.repository.add_screenshot(
                context.scan_id,
                image.stem,
                str(image)
            )
    
        print(
            f"[+] Stored screenshots from {output_dir}"
        )