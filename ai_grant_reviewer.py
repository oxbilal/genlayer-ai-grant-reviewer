# { "Depends": "py-genlayer:test" }

from genlayer import *

class AIGrantReviewer(gl.Contract):
    last_result: str

    def __init__(self):
        self.last_result = ""

    def _ask_ai(self, proposal: str):
        prompt = f"""
Review this grant proposal:
{proposal}

Return JSON only with:
score: number from 1 to 10
decision: approve, revise, or reject
strength: short text
risk: short text
suggestion: short text
"""
        return gl.nondet.exec_prompt(prompt, response_format="json")

    def _validator(self, leader_result) -> bool:
        if not isinstance(leader_result, gl.vm.Return):
            return False

        data = leader_result.calldata
        return (
            isinstance(data, dict)
            and isinstance(data.get("score"), int)
            and 1 <= data.get("score") <= 10
            and data.get("decision") in ["approve", "revise", "reject"]
            and isinstance(data.get("strength"), str)
            and isinstance(data.get("risk"), str)
            and isinstance(data.get("suggestion"), str)
        )

    @gl.public.write
    def review_proposal(self, proposal: str):
        result = gl.vm.run_nondet_unsafe(
            lambda: self._ask_ai(proposal),
            self._validator
        )
        self.last_result = str(result)

    @gl.public.view
    def get_last_review(self) -> str:
        return self.last_result
