"""

RenderPipeline

Copyright (c) 2014-2016 tobspr <tobias.springer1@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from ...pluginbase.base_plugin import BasePlugin
from ...stages.ambient_stage import AmbientStage
from ...stages.apply_lights_stage import ApplyLightsStage

from .ao_stage import AOStage

class Plugin(BasePlugin):

    name = "Ambient Occlusion"
    author = "tobspr <tobias.springer1@gmail.com>"
    description = ("A plugin to render ambient occlusion supporting multiple"
                   "techniques such as SSAO, HBAO and much more ")
    version = "1.1"

    def on_stage_setup(self):
        self._stage = self.create_stage(AOStage)

        # Make the stages use our output
        AmbientStage.required_pipes.append("AmbientOcclusion")
        ApplyLightsStage.required_pipes.append("AmbientOcclusion")
