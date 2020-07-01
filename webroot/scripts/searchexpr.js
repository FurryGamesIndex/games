 /* 
  * Copyright (C) 2020 Utopic Panther
  * 
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
  * 
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  * 
  * You should have received a copy of the GNU General Public License
  * along with this program.  If not, see <https://www.gnu.org/licenses/>.
  */ 

(() => {
const TOKEN_TYPE = {
	LEFT_BRACKETS: 1,
	RIGHT_BRACKETS: 2,
	STRING: 3,
	AND: 4,
	OR: 5,
	NOT: 6,
	INVALID: 0
};

function Token(type, value) {
	this.type = type;
	this.value = value;
}

const lexer = expr => {
	const list = [];
	let token = "";

	let pop_staging_token = () => {
		switch (token) {
		case "":
			break;
		case "and":
			list.push(new Token(TOKEN_TYPE.AND));
			break;
		case "or":
			list.push(new Token(TOKEN_TYPE.OR));
			break;
		case "not":
			list.push(new Token(TOKEN_TYPE.NOT));
			break;
		default:
			list.push(new Token(TOKEN_TYPE.STRING, token));
			break;
		}
		token = "";
	}

	for (let i = 0; i <= expr.length; i++) {
		let end;
		const chr = expr.charAt(i);

		console.log(i + " " + chr)

		switch (chr) {
		case "":
		case " ":
		case "\t":
			pop_staging_token();
			break;
		case "(":
			pop_staging_token();
			list.push(new Token(TOKEN_TYPE.LEFT_BRACKETS));
			break;
		case ")":
			pop_staging_token();
			list.push(new Token(TOKEN_TYPE.RIGHT_BRACKETS));
			break;
		case '"':
			end = expr.substring(i + 1).indexOf('"');
			if (end < 0)
				throw "error while compiling expression: missing terminating '\"' character. at " + i;
			//if (i + end < i) {
			//	list.push(new Token(TOKEN_TYPE.STRING, ""))
			//} else {
				list.push(new Token(TOKEN_TYPE.STRING, expr.substring(i + 1, i + end + 1)))
			//}
			i += end + 1;
			break;
		default:
			token += chr
			break;
		}
	}
	return list;
}

const searchexpr = (expr, callback) => {
	const tokens = lexer(expr);
	console.log("searchexpr: debug: lexing done.");
	console.log(tokens);


}

window.searchexpr = searchexpr;
})();

expr = 'y:abcd and x:efg or (fui:a and "a:sys no" not "") and (("ccc") or (axd and amd))';
searchexpr(expr, null)
