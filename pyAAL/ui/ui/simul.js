//////////////////////////////////////////////////////////
//
//  AccLab UI : simul.js
//
// Copyright (C) 2016 Walid Benghabrit
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//////////////////////////////////////////////////////////

visualEditor.ui.simul = {

    TestCommands: {
        ls: function () {
            // Fake 'ls' command for demo purposes
            this.write('LICENSE\nMakefile\nREADME.md\nbuild/\nbuild.js\nexamples/\nsrc/\nvendor/\n');
            this.exit();
        },

        ll: function () {
            TestCommands.ls.call(this, arguments);
        },

        help: function () {
            this.write('Press < tab > to see a list of available commands.');
            this.exit();
        },

        cd: function () {
            // Fake 'cd' command for demo purposes
            this.write('Sorry, access not granted');
            this.exit();
        },

        exit: function () {
            location.reload();
        },

        sum: function (op1, op2) {
            if (arguments.length < 2)
                this.write('Please insert two numeric values (ex. > sum 5 6)', 'stderr');
            else
                this.write(parseInt(op1, 10) + parseInt(op2, 10));

            this.exit();
        },

        echo: function () {
            var args = Array.prototype.slice.call(arguments, 0);
            this.write(args.join(' '));

            this.exit(0);
        }
    },

    showConsole: function(title) {
        $("body").append("<div id='terminal-app"+title+"'></div>");
        var target = '#terminal-app'+title;
        var terminalWin = visualEditor.wm.createWindow.fromQuery(target, {
            title: title,
            x: 60,
            y: 50,
            width: 450,
            height: 300,
            classname: 'terminal-window',
            widget: false,
            titlebar: true,
            events: {
                closed: function() {
                    this.destroy();
                }
            }
        });

        terminalWin.signals.on('click', function(win){
			terminal.display.focus();
		});

        var terminal = new Terminus(target, {
				welcome: "<div class='identity'><h1>Welcome to " +title+ " shell</h1> "+
                "</div>.<br/>Press <span style='color:green'>&lt; tab &gt;</span> " +
                "to see a list of available commands."
			});
        terminal.shell.include([this.TestCommands]);

		terminal.display.events.on('prompt', function() {
			terminalWin.$content.animate({
				scrollTop:terminalWin.el.find('.terminusjs').height()
			}, 300);
		});

        terminalWin.open();
    }
};
