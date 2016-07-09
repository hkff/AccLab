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

function command(doc, fx) {
    fx.__doc__ = doc;
    return fx;
}

visualEditor.ui.simul = {
    simulation: null,
    name: "",
    monitor_port: 9999,
    currentTerminal: null,
    monitor_backend: "",
    passkey: "1234",

    /**
     * Actor data type
     * @param agent
     * @param time
     * @param location
     * @returns actor object
     * @constructor
     */
    Actor: function(agent, time, location) {
        return {
            name: agent,
            terminal: null,
            aal_policy: "",
            formula: "G(true)",
            kv: [],
            data: [],
            trace: [],
            violations: [],
            location: "France",
            time: "0",
            monitor_enabled: true,
            rt_control: false,

            /**
             * Run the monitor and get the result
             * @returns {string}
             */
            monitor: function() {
                var name = this.name;
                var res = "?";
                $.ajax({
                    dataType: 'text',
                    type:'POST',
                    url: visualEditor.ui.simul.monitor_backend + "/api/actor/monitor/run",
                    data: {actor: name, sys: visualEditor.ui.simul.name},
                    async: false,
                    crossDomain: true,
                    success: function(response) {
                        res = response;
                    }
                });
                return res;
            },

            /**
             * Register actor
             * @returns {string}
             */
            register: function() {
                var res = "";
                var _this = this;
                $.ajax({
                    dataType: 'text',
                    type:'POST',
                    url: visualEditor.ui.simul.monitor_backend + "/api/actor/register",
                    data: {actor: _this.name, formula: _this.formula, trace:"{}", sys: visualEditor.ui.simul.name},
                    async: false,
                    crossDomain: true,
                    success: function(response) {
                        console.log(response);
                        res = response;
                    }
                });
                return res;
            },

            /**
             * Get actor's knowledge vector
             * @returns {string}
             */
            getKV: function() {
                var res = "";
                var _this = this;
                $.ajax({
                    dataType: 'text',
                    type:'POST',
                    url: visualEditor.ui.simul.monitor_backend + "/api/actor/kv",
                    data: {actor: _this.name, sys: visualEditor.ui.simul.name},
                    async: false,
                    crossDomain: true,
                    success: function(response) {
                        console.log(response);
                        res = response;
                    }
                });
                return res;
            },

            /**
             * Push an event into actor's trace and send it to the monitor.
             * @param event
             */
            pushEvent: function(event) {
                this.trace.push(event);
                var name = this.name;
                $.ajax({
                    dataType: 'text',
                    type:'POST',
                    url: visualEditor.ui.simul.monitor_backend + "/api/actor/events/push",
                    data: {actor: name, event: event, sys: visualEditor.ui.simul.name},
                    async: true,
                    crossDomain: true,
                    success: function(response) {
                        console.log(response);
                    }
                });
            }
        }
    },

    /**
     * Local data object
     * @param name
     * @param types
     * @returns {{name: *, types: *}}
     * @constructor
     */
    Data: function(name, types) {
        return {name: name, types: types}
    },

    /**
     * Start the simulation and the remote Fodtlmon service
     * @param port
     */
    startSimulation: function(port) {
        this.name = "Simulation1";
        this.monitor_port = port;
        this.monitor_backend = "http://127.0.0.1:" + port;
        this.simulation = {actors: {}};

        // Start monitoring server
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.backend,
            async: false,
            data: {action: "startSimulation", port: this.monitor_port},
            success: function(response) {}
        });

        // 1. Analyse current ACD file and extract all actors with policies
        var actors = visualEditor.ui.canvas.getFigures().data.filter(function(e){return e.type === "Actor"});
        var clauses = visualEditor.ui.canvas.getFigures().data.filter(function(e){return e.type === "Policy"});
        for(var i=0; i<actors.length; i++) {
            var agent = actors[i].getName();
            this.simulation.actors[agent] = this.Actor(agent);
        }

        // Register the new system
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.ui.simul.monitor_backend + "/api/system/create",
            data: {sys_name: this.name},
            async: true,
            crossDomain: true,
            success: function(response) {
                console.log(response);
            }
        });
    },

    /**
     * Stop the simulation and the Fodtlmon service
     */
    stopSimulation: function() {
        // Close all terminals
        $.each(visualEditor.ui.simul.simulation.actors, function(i, v) {if(v.terminal != null) v.terminal.close()});

        this.simulation = null;
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.ui.simul.monitor_backend + "/api/shutdown",
            data: {passkey: visualEditor.ui.simul.passkey},
            async: true,
            crossDomain: true,
            success: function(response) {
                console.log(response);
            }
        });
    },

    /**
     * Simulation commands
     */
    SimulationCommands: {

        ll: function () {
            //SimulationCommands.ls.call(this, arguments);
        },

        autoSetup: command(
            "Admin only: Auto configure the simulation",
            function() {
                // TODO
                this.write("Attaching actors policies...");
                this.write("Registering actors...");
                this.write("Done.");
                this.exit();
            }),

        exit: command(
            "Close the terminal.",
            function() {
                this.exit();
                visualEditor.ui.simul.currentTerminal.win.close();
            }),

        spoof: command(
            "Spoof an agent id to perform an action.\nUsage: spoof <<actor_name>> <<action>>",
            function(actor, action) {
                // TODO
                this.write('Spoof');
                this.exit();
            }),

        compilePolicy: command(
            "Compile actor's policy into FODTL formula and put it in the formula.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var clause = visualEditor.ui.simul.simulation.actors[actor].aal_policy;
                var file = visualEditor.ui.getOpenedFile().replace('acd', 'aal');
                this.write("Compiling...");
                $.ajax({
                    dataType: 'text',
                    type:'POST',
                    url: visualEditor.backend,
                    data: {action: "aal_to_fodtl", file: file, clause: clause},
                    async: false,
                    success: function(response) {
                        visualEditor.ui.simul.simulation.actors[actor].formula = response;
                    }
                });
                this.exit();
            }),

        setFormula: command(
            "Change actor's formula.\nUsage: formula <<fodtl formula>>",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                visualEditor.ui.simul.simulation.actors[actor].formula = Array.prototype.slice.call(arguments, 0).join(" ");
                this.exit();
            }),

        formula: command(
            "Show actor's formula.\nUsage: formula",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var res = visualEditor.ui.simul.simulation.actors[actor].formula;
                this.write(res);
                this.exit();
            }),

        register: command(
            "Register actor.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var res = visualEditor.ui.simul.simulation.actors[actor].register();
                this.write(res);
                this.exit();
            }),

        setTime: command(
            "Change actor's time.\nUsage: setTime <<time>>" +
            "\n Examples:" +
            "\n - time 3   // Set current actor's time to 3",
            function(time) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                visualEditor.ui.simul.simulation.actors[actor].time = time;
                this.exit();
            }),

        time: command(
            "Show actor's local time.\nUsage: time [actor_name]" +
            "\n Examples:" +
            "\n - time     // Show current actor's time"+
            "\n - time bob // Show bob's time",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                this.write(visualEditor.ui.simul.simulation.actors[actor].time);
                this.exit();
            }),

        setLocation: command(
            "Change actor's location.\nUsage: setLocation <<location_name>>" +
            "\n Examples:" +
            "\n - location  france   // Set current actor's location to france",
            function(location) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                visualEditor.ui.simul.simulation.actors[actor].location = location;
                this.exit();
            }),

        location: command(
            "Show actor's location.\nUsage: location [actor_name]" +
            "\n Examples:" +
            "\n - location     // Show current actor's location"+
            "\n - location bob // Show bob's location",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                this.write(visualEditor.ui.simul.simulation.actors[actor].location);
                this.exit();
            }),

        violations: command(
            "Show actor violations.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var res = visualEditor.ui.simul.simulation.actors[actor].violations;
                this.write(res);
                this.exit();
            }),

        kv: command(
            "Show local monitor's knowledge vector.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var res = visualEditor.ui.simul.simulation.actors[actor].getKV();
                this.write(res);
                this.exit();
            }),

        trace: command(
            "Show actor trace.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                this.write(visualEditor.ui.simul.simulation.actors[actor].trace);
                this.exit();
            }),

        monitor: command(
            "Enable/disable the reference monitor.\nUsage: monitor <<on/off>>",
            function() {
                this.write('Monitoring');
                this.exit();
            }),

        run: command(
            "Perform a service call by the agent.\nUsage: run service[actor](args)",
            function(action) {
                // TODO check with regexp
                var service = action.substring(0, action.indexOf("["));
                var targetName = action.substring(action.indexOf("[")+1, action.indexOf("]"));
                var actionArgs = action.substring(action.indexOf("(")+1, action.indexOf(")"));
                if(actionArgs == "") actionArgs = "NONE";

                var actorName = visualEditor.ui.simul.currentTerminal.agent;
                var actor = visualEditor.ui.simul.simulation.actors[actorName];
                var target = visualEditor.ui.simul.simulation.actors[targetName]; // TODO check

                var currentActorUI = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Actor" && e.getName() == actorName});

                var targetActorUI = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Actor" && e.getName() == targetName});

                var consUI = null;

                if(currentActorUI.length > 0 && targetActorUI.length > 0) {
                    currentActorUI = currentActorUI[0];
                    targetActorUI = targetActorUI[0];
                    var s1 = currentActorUI.RSO.data.filter(function (e) {
                        return e.text == service
                    });
                    var s2 = targetActorUI.PSO.data.filter(function (e) {
                        return e.text == service
                    });
                    if (s1.length > 0 && s2.length > 0) {
                        var cons = s1[0].getConnections();
                        // TODO select the correct connexion
                        if (cons.data.length > 0) {
                            consUI = cons.get(0);
                            var old_color = consUI.getColor();
                            consUI.setColor("#230990");
                            // 1. Animate connection
                        }
                    }

                    // 2. Log the event in current actor trace
                    var ac = service+"("+actorName+","+targetName+","+actionArgs+")";
                    var location = "LOCATION('" + actorName + "', '" + actor.location + "')";
                    var time = "TIME('" + actorName + "', '" + actor.time + "')";
                    var event = "{" +ac+"|"+ location + "|" + time + "}";
                    actor.pushEvent(event);

                    // 3. Monitor and get the result
                    if(actor.monitor_enabled) {
                        var mon_res = actor.monitor();
                        this.write(mon_res);
                        if(mon_res == "false") {
                            actor.violations.push("Violation");
                            if(actor.rt_control) {
                                this.write("Violation");
                                this.exit();
                                return;
                            }
                        }
                    }

                    // 4. Simulate the network

                    // if received:
                    // Update target KV
                     $.ajax({
                        dataType: 'text',
                        type:'POST',
                        url: visualEditor.ui.simul.monitor_backend + "/api/actor/updatekv",
                        data: {actor: targetName, sys: visualEditor.ui.simul.name, from: actorName},
                        async: false,
                        crossDomain: true,
                        success: function(response) {
                            console.log(response);
                        }
                    });
                    // 5. Log the event in target actor trace

                        // 6. Run target's monitor
                            // if monitor enabled
                                // if res is false
                                    // report violation

                    this.write('calling:' + service + " on " + targetName + " with " + actionArgs);
                    this.exit();
                 } else {
                    this.write("Error actors not found !");
                    this.exit();
                }
            }),

        rm: command(
            "Remove a local data.\nUsage: rm <<data_name>>",
            function(name) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var data = visualEditor.ui.simul.simulation.actors[actor].data;
                var deleted = false;
                for(var i=0; i<data.length; i++) {
                    if(data[i].name == name) {
                        data.splice(i, 1);
                        deleted = true;
                        this.write("Data deleted !");
                    }
                }
                if(!deleted)
                    this.write("Data not found !");
                this.exit();
            }),

        showData: command(
            "Show local data of an actor. If actor_name is not specified it shows current actor data" +
            "\nUsage: show_data [actor name]",
            function(name) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                if(name != undefined)
                    var data = visualEditor.ui.simul.simulation.actors[actor].data;
                else
                    var data = visualEditor.ui.simul.simulation.actors[name].data; // TODO check
                for(var i=0; i<data.length; i++)
                    this.write(data[i].name + ':' + data[i].types + '\n');
                this.exit();
            }),

        data: command(
            "Create a local data.\nUsage: data name type1 type2 ... typeN",
            function(name) {
                if(name != undefined) {
                    // TODO check if data exsits
                    var actor = visualEditor.ui.simul.currentTerminal.agent;
                    var types = [];
                    if(arguments.length > 1)
                        types = Array.prototype.slice.call(arguments, 0).slice(1);
                    var d = visualEditor.ui.simul.Data(name, types);
                    visualEditor.ui.simul.simulation.actors[actor].data.push(d);
                    this.write('Data stored ! ');
                } else
                    this.write('Error no name given! ');
                this.exit();
            }),

        attach: command(
            "Attach the given policy to the agent.\nUsage: attach <<policy_name>>",
            function(policy) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var clauses = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Policy" && e.tlabel.text == policy});
                if(clauses.length > 0) {
                    visualEditor.ui.simul.simulation.actors[actor].aal_policy = policy;
                    this.write("Policy " + policy + " attached successfully !");
                } else
                    this.write("Error: policy " + policy + " not found !");
                this.exit();
            }),

        policy: command(
            "Show AAL policy attached to the current actor.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var policy = visualEditor.ui.simul.simulation.actors[actor].aal_policy;
                var clauses = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Policy" && e.tlabel.text == policy});
                if(clauses.length > 0)
                    this.write(clauses[0].policy);
                else
                    this.write("Error: policy " + policy + " not found !");
                this.exit();
            }),

        policyName: command(
            "Show AAL policy name attached to the current actor.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var policy = visualEditor.ui.simul.simulation.actors[actor].aal_policy;
                this.write(policy);
                this.exit();
            }),

        clear: command(
            "Clear console.",
            function() {
                visualEditor.ui.simul.currentTerminal._display.output.clear();
                this.exit();
            }),

        man: command(
            "Show manual of a command.\nType man <<command_name>> to print command help.",
            function(cmd) {
                if(arguments.length > 0) {
                    if(visualEditor.ui.simul.SimulationCommands.hasOwnProperty(cmd)) {
                        this.write(visualEditor.ui.simul.SimulationCommands[cmd].__doc__);
                    } else
                        this.write('Command not found ! Press < tab > to see a list of available commands.');
                }  else
                    this.write('Type man <<command_name>> to print command help.');
                this.exit();
            }),

        help: command(
            "Show this help. Type help <<command_name>> to print command help",
            function() {
                this.write('Press < tab > to see a list of available commands.\nType man <<command>> to print command manual.');
                this.exit();
            })
    },

    /**
     * Show actor's console
     * @param actor
     */
    showConsole: function(actor) {
        // Check if simulation is running
        if(visualEditor.ui.simul.simulation == null) {
            toastr.error("No simulation is running !");
            return;
        }

        var target = '.terminal-app-'+actor;
        // Avoid multiple terminals for same actor
        if($(target).length > 0)
            return;

        $("body").append("<div class='terminal-app-"+actor+"'></div>");
        var terminalWin = visualEditor.wm.createWindow.fromQuery(target, {
            title: actor,
            x: 60,
            y: 50,
            width: 500,
            height: 300,
            classname: 'terminal-window',
            widget: false,
            titlebar: true,
            events: {
                closed: function() {
                    this.destroy();
                    if(visualEditor.ui.simul.simulation != null)
                        visualEditor.ui.simul.simulation.actors[actor].terminal = null;
                }
            }
        });

        terminalWin.signals.on('click', function(win) {
			terminal.display.focus();
            visualEditor.ui.simul.currentTerminal = terminal;
		});

        var terminal = new Terminus(target, {
				welcome: "<div class='identity'><h1>Welcome to " +actor+ "'s shell</h1></div>"+
                "Press <span style='color:green'>&lt; tab &gt;</span> " + "to see a list of available commands."
			});
        terminal.shell.include([this.SimulationCommands]);
        terminal.agent = actor;
        terminal.win = terminalWin;
        visualEditor.ui.simul.simulation.actors[actor].terminal = terminalWin;

		terminal.display.events.on('prompt', function() {
			terminalWin.$content.animate({scrollTop:terminalWin.el.find('.terminusjs').height()}, 300);
		});

        // Open the terminal
        terminalWin.open();
    }
};
