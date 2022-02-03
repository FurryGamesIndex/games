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
	INIT: 7,
	ACTION_ORDER: 8,
	INVALID: 0
};

function Token(type, value) {
	this.type = type;

	if (type == TOKEN_TYPE.STRING) {
		switch (value[0]) {
		case "@":
			this.type = TOKEN_TYPE.ACTION_ORDER;
			value = value.substring(1);
			break;
		case "$":
			this.type = TOKEN_TYPE.INVALID;
			break;
		}
	}

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

			list.push(new Token(TOKEN_TYPE.STRING, expr.substring(i + 1, i + end + 1)))
			i += end + 1;
			break;
		default:
			token += chr
			break;
		}
	}
	return list;
}

const interpreter = (tokens, pos, callback) => {
	let s = new Set();
	let state = TOKEN_TYPE.INIT;
	let temp;

	const intpDoAndOrNot = (s1, s2) => {
		const cstate = state;
		state = TOKEN_TYPE.AND;

		switch (cstate) {
		case TOKEN_TYPE.AND:
			return new Set([...s1].filter(v => s2.has(v)));
			break;
		case TOKEN_TYPE.OR:
		case TOKEN_TYPE.INIT:
			return new Set([...s1, ...s2]);
			break;
		case TOKEN_TYPE.NOT:
			return new Set([...s1].filter(v => !s2.has(v)));
			break;
		}
		return new Set();
	}

	const intpReOrder = (s, cmd) => {
		switch (cmd) {
		case "reverse":
			return new Set([...s].reverse());
			break;
		case "lastmod":
        case "lastpost":
			return new Set([...s].sort((fe, se) => {
				return callback("$sortcmpr", {
					sortedBy: cmd,
					firstElm: fe,
					secondElm: se
				});
			}));
			break;
		}
		throw "Unknown order action \"" + cmd + "\"."
	}

	const intpSubExprRequireLoadAll = () => {
		if (state === TOKEN_TYPE.INIT)
			s = new Set(callback('$all'));
			state = TOKEN_TYPE.AND;
	}

	while (pos < tokens.length) {
		switch (tokens[pos].type) {
		case TOKEN_TYPE.LEFT_BRACKETS:
			const retv = interpreter(tokens, pos + 1, callback);
			s = intpDoAndOrNot(s, retv[1]);
			pos = retv[0]
			break;
		case TOKEN_TYPE.RIGHT_BRACKETS:
			return [pos, s];
			break;
		case TOKEN_TYPE.STRING:
			temp = new Set(callback(tokens[pos].value));
			s = intpDoAndOrNot(s, temp);
			break;
		case TOKEN_TYPE.AND:
		case TOKEN_TYPE.OR:
			state = tokens[pos].type;
			break;
		case TOKEN_TYPE.NOT:
			intpSubExprRequireLoadAll();
			state = tokens[pos].type;
			break;
		case TOKEN_TYPE.ACTION_ORDER:
			intpSubExprRequireLoadAll();
			s = intpReOrder(s, tokens[pos].value);
			break;	
		}
		pos++;
	}
	return [pos, s];
}

const searchexpr = (expr, callback) => {
	const tokens = lexer(expr);
	console.log("searchexpr: debug: lexing done.");
	console.log(tokens);

	return interpreter(tokens, 0, callback)[1];
}

window.searchexpr = searchexpr;
})();
