import json
from pathlib import Path
import time


class HubBaseParams:
    def __init__(self, paramsstr: str):
        self.params = self.str_to_list(paramsstr)

    @staticmethod
    def str_to_list(value: str | list, *, reverse: bool = False) -> str | list[str]:
        if reverse:
            return f"({', '.join(list[str](value))})"
        else:
            value = str(value).removeprefix("(").removesuffix(")").split(", ")
            return value

    def __str__(self) -> str:
        return str(self.str_to_list(self.params, reverse=True))


class HubBaseVersion:
    def __init__(self, version: str | list, params: HubBaseParams, *, Features: list[str] | str = ""):
        self.rawversion: str = str(version)
        if isinstance(version, str):
            version = self.str_to_list(version)
        if len(version) in (7, 8):
            self.version = version
        else:
            raise TypeError("Expected 7-part version string/list.")
        self.params = params
        self.features = list[str](Features)

    def str_to_list(self, value: str | list, *, reverse: bool = False) -> str | list[str | int]:
        if reverse:
            value = self.rawversion
        else:
            value = str(value).split(".")
            if len(value) not in (5, 6):
                raise TypeError("Expected 4 or 5 dots in version.")
            ndvp = value[4]
            value.remove(ndvp)
            ndvp = [ndvp[0] + ndvp[1],
                    ndvp.removeprefix(ndvp[0] + ndvp[1]).removesuffix(ndvp[-1]),
                    ndvp[-1] if len(ndvp) > 2 else ""
                ]
            try:
                extras = value[4]
                value.remove(extras)
                ndvp.append(extras)
            except IndexError:
                pass
            for x in ndvp:
                value.append(x)
        return value

    def getfeatures(self, returnstr: bool = False):
        if returnstr:
            text = "Features: \n"
            for feature in self.features:
                text += f"    - {feature} \n"
            return text
        else:
            return self.features


    def __str__(self) -> str:
        return f"{self.str_to_list(self.version, reverse=True)} {str(self.params)}"


versions = []
with open(Path(__file__).resolve().parent / "Data" / "versions.json", "r", encoding="utf-8") as f:
    content = json.load(f)
for version, info in content.items():
    versions.append(HubBaseVersion(version, info["params"], Features=info["features"]))


def view_log():
    D1 = input("The Main part -- ").lower()
    D2 = input("The addition -- ")
    D3 = input("The fix -- ")
    print("0.00, 0.01, ..., 0.10, 1.00, and so on")
    D4 = input("Extras -- ")
    print("a(n) - for alphas, b(n) - for betas, rc(n) - for prereleases, f - for releases")
    D5 = input("Access to Version -- ").lower().replace("f", "")
    print("The security updates are exclusive to the wiki!")
    print("")
    searchfor = f"{D1}.{D2}.{D3}.{D4}{D5}"
    try:
        print(find_version_info(fullstr=searchfor, addfeatures=True))
    except NotImplementedError:
        print(f"Version {searchfor} does not exist, or is not documented.")


def find_version_info(D1 = None, D2 = None, D3 = None, D4 = None, D5 = None, *, fullstr: str | None = None, addfeatures: bool = False) -> str:
    if fullstr is None:
        searchfor = f"{D1}.{D2}.{D3}.{D4}{D5}"
    else:
        searchfor = fullstr
    for version in versions:
        if version.str_to_list(version.version, reverse=True) == searchfor:
            if addfeatures: return f"=== HubBase v{version} {version.params} === \n{version.getfeatures(True)}"
            else: return f"=== HubBase v{version} {version.params} === "
    raise NotImplementedError(f"Version {searchfor} does not exist, or is not documented.")


if __name__ == '__main__':
    view_log()
    time.sleep(3)
